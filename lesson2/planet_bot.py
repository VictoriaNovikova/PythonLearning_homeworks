from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import logging
import datetime
from dateutil.parser import parse
import re
from Constellation import Constellation

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='planet_bot.log'
                    )

def greet_user(bot, update):
    text = """ Привет, {}!
Я могу отвечать на вопросы о планетах. Я понимаю команды вида "/planet Mars" или "Когда ближайшее полнолуние после 09.09.2017?"
    """.format(update.message.chat.first_name)
    update.message.reply_text(text)

planets = {
    "Марс": "Mars",
    "Луна": "Moon",
    "Юпитер": "Jupiter",
    "Солнце": "Sun",
    "Меркурий": "Mercury",
    "Венера": "Venus",
    "Уран": "Uranus",
    "Сатурн": "Saturn",
    "Нептун": "Neptune",
    "Земля": "Earth"
}

def planet(bot, update, args):
    if len(args) == 0:
        update.message.reply_text("Введите планету")
        return

    for user_text in args:
        try:
            user_planet = planets.get(user_text, user_text)
            planet = getattr(ephem, user_planet)
        except AttributeError:
            update.message.reply_text("Извини, я не знаю планету {}".format(user_text))
            continue
        answer = ephem.constellation(planet(datetime.datetime.now()))
        update.message.reply_text("{} сейчас в созвездии {}".format(user_text, Constellation.get(answer[0], answer[0])))

def next_full_moon(bot, update):
    text =  update.message.text
    match_with_date = re.match("(?:\w+\s?)*(полно|ново)луние(?:\s?)после (\d{2}[\.\/-]\d{2}[\.\/-]\d{4})\??", text.lower())
    match_today=re.match("(?:\w+\s?)*(полно|ново)луние?", text)
    match = match_with_date if match_with_date else match_today
    if match:
        try:
            date = parse(match.group(2)) if match_with_date else datetime.datetime.now()            
        except ValueError:
            update.message.reply_text("Что-то пошло не так! Ты уверен, что число %s верное?" % match.group(2))
            return
        if match.group(1) == "полно":
            result = ephem.next_full_moon(date)
        else:
            result = ephem.next_new_moon(date)            
        update.message.reply_text("Ближайшее {}луние будет в {:%H:%M %d.%m.%Y}".format(match.group(1),result.datetime()))
        return
    elif "привет" in text.lower():
        update.message.reply_text("И тебе привет, {}!".format(update.message.chat.first_name))
        return
    elif "пока" in text.lower():
        update.message.reply_text("Пока, {}! Пиши еще.".format(update.message.chat.first_name))
        return
    update.message.reply_text("Попробуй спросить что-нибудь еще")


def main():
    # @learn_python_planet_bot
    updater = Updater('416947667:AAGS5F_PBO4jTE8WQq9-LLKvf9j_8tiNGuo')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, next_full_moon))
    updater.start_polling()
    updater.idle()

main()