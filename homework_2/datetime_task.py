from datetime import datetime, timedelta


dt_now = datetime.now()
print("Сегодня - {}".format(dt_now.strftime('%d.%m.%Y')))
print("Вчера было - {}".format((dt_now - timedelta(days=1)).strftime('%d.%m.%Y')))
print("Месяц назад было - {}".format((dt_now - timedelta(weeks=4)).strftime('%d.%m.%Y')))


date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print(type(date_dt))
