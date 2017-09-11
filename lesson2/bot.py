from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import logging
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet(bot, update, args):
    if len(args) == 0:
        update.message.reply_text("Введите планету")
        return

    for user_planet in args:
        try:
            planet = getattr(ephem, user_planet)
        except AttributeError:
            update.message.reply_text("Извини, такой планеты {} нет".format(user_planet))
            continue
        answer = ephem.constellation(planet(datetime.datetime.now()))
        update.message.reply_text("{} сейчас в созвездии {}".format(user_planet, answer[1]))


def word_count(bot, update, args):
    if len(args) == 0:
        update.message.reply_text("Нет строки для подсчета")
        return
    
    update.message.reply_text('Всего слов - {}'.format(len(args)))

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    updater = Updater('442826411:AAFKyhyINogOlVSD1_gnaebTD5KEXbDYm1w')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", word_count, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

main()