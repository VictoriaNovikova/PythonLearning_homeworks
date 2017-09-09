age = int(input("Пожалуйста введите Ваш возраст "))
print("Ваш род занятий:")
if age <= 7:
    print("Детский сад")
elif age in range(7, 18):
    print("Школа")
elif age in range(18, 23):
    print("ВУЗ")
else:
    print("Работа")