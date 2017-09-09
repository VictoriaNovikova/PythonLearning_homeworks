def strip(word):
    stripped = word.strip()
    for char in ["!", "?", "."]:
        stripped = stripped.strip(char)
    return stripped

def get_answer(question):
    return {
        "как дела": "Отлично",
        "привет": "Привет",
        "как настроение": "Хорошо",
        "как погода": "Ужас!!",
        "какой ответ на самый главный вопрос жизни, вселенной и всего такого": 42,
        "пока": "Пока!"
    }.get(strip(question.lower()), "Спроси еще что-нибудь")


def ask_user():
    while True:
        user_ask = input('Спроси меня о чем нибудь ')
        print(get_answer(user_ask))
        if strip(user_ask.lower()) == "пока":
            break

ask_user()

