from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import operator
import re

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='calc_bot.log'
                    )

def greet_user(bot, update):
    text = """ Привет, {}!
Я маленький бот-калькулятор. Я понимаю команды вида "1+2=" или "Сколько будет один плюс два?" (но так я умею считать только до 20)
    """.format(update.message.chat.first_name)
    update.message.reply_text(text)

def calculate_expression(expression):
    expression = expression.strip("=")
    operations = {
        "+": operator.add,
        '*': operator.mul,
        '-': operator.sub,
        '%': operator.mod,
        '<': operator.lt,
        '/': operator.truediv
    }
    
    for operation in operations.keys():
        if operation in expression:
            nums = []
            for num in expression.split(operation):
                try:
                    num = int(num)
                except (ValueError, TypeError):
                    try:
                        num = float(num)
                    except (ValueError, TypeError):
                        return "Что-то пошло не так"
                nums.append(num)
            if len(nums) != 2:
                return "Извини, я могу обрабатывать только два числа"
            try:
                result = operations[operation](nums[0], nums[1])
            except ZeroDivisionError:
                return "Ты же знаешь, делить на 0 нельзя!"
            return "Я все посчитал! Результат: {}".format(result)
    return "Я не смог, попробуй другую операцию. :("

def parse_and_calculate(first, operation, second):
    numbers = {
        'один': '1',
        'два': '2',
        'три': '3', 
        'четыре': '4',
        'пять': '5',
        'шесть': '6',
        'семь': '7',
        'восемь': '8',
        'девять': '9',
        'десять': '10',
        'ноль': '0',
        'одиннадцать': '11',
        'двенадцать': '12',
        'тринадцать': '13',
        'четырнадцать': '14',
        'пятнадцать': '15',
        'шестнадцать': '16',
        'семнадцать': '17',
        'восемнадцать': '18',
        'девятнадцать': '19',
        'двадцать': '20'
    }
    operations = {
        'плюс': '+',
        'минус': '-',
        'умножить на': '*',
        'разделить на': '/',
        'по модулю': '%'
    }
    def parse_number(number):
        return "{integer}{dot}{fractional}".format(integer=numbers.get(number[0], number[0]), dot = "." if number[1] != "" else "", fractional=numbers.get(number[2], number[2]))


    parsed = parse_number(first) + operations.get(operation, "") + parse_number(second)
    return calculate_expression(parsed)

def calculate(bot, update):
    expression = update.message.text
    result = ""
    match = re.match("[Сс]колько будет (\w+)\s?(и|точка|\.|)\s?(\w*) (плюс|минус|умножить на|разделить на|по модулю) (\w+)\s?(и|точка|\.|)\s?(\w*)\??", expression)
    if match:
        result =parse_and_calculate(first=(match.groups(0)[0], match.groups(0)[1], match.groups(0)[2]), operation=match.groups(0)[3], second=(match.groups(0)[4], match.groups(0)[5], match.groups(0)[6]))
    elif str.endswith(expression, "="):
        result = calculate_expression(expression)
    elif "привет" in expression.lower():
        result = "И тебе привет, {}!".format(update.message.chat.first_name)
    elif "пока" in expression.lower():
        result = "Еще увидимся!"
    else:
        result ="Вводите, пожалуйста, правильные команды"
    update.message.reply_text(result)

def main():
    # @learn_python_calc_bot
    updater = Updater('363248772:AAEbGDZLs2aOzeWCPXQJUCbrhRGnHTPsPx8')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, calculate))
    updater.start_polling()
    updater.idle()

main()