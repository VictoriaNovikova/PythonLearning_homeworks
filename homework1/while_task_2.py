def ask_user():
    while True:
        user_say = input('Как дела? ')
        if user_say.lower().strip() == "хорошо":
            print("Отлично!")
            break

ask_user()