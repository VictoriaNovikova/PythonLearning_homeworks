def find_person(name, names):
    persons = names.copy()
    if (len(persons) == 0):
        print("Список пуст! Искать негде")
        return
    person = persons.pop(0)
    while person != name and len(persons) != 0:
        person = persons.pop(0)
    if person == name:
        print("{} нашелся".format(name))
    else:
        print("{} тут нет".format(name))


names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
find_person("Валера", names)
find_person("Даша", names)
find_person("Вика", names)