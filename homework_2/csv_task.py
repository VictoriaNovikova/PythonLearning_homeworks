import csv

answers = [
            {'question': "как дела", 'answer': "Отлично"},
            {'question': "привет", 'answer': "Привет"},
            {'question': "как настроение", 'answer': "Хорошо"},
            {'question': "как погода", 'answer': "Ужас!!"},
            {'question': "какой ответ на самый главный вопрос жизни, вселенной и всего такого", 'answer': "42"},
            {'question': "пока", 'answer': "Пока!"}
        ]

with open('export.csv', 'w', encoding='utf-8') as file_to_write:
    fields = ['question', 'answer']
    writer = csv.DictWriter(file_to_write, fields, delimiter=';')
    writer.writeheader()
    for user_answer in answers:
        writer.writerow(user_answer)