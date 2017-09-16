from datetime import datetime, timedelta, date
from calendar import monthrange


dt_now = datetime.now()
print("Сегодня - {}".format(dt_now.strftime('%d.%m.%Y')))
print("Вчера было - {}".format((dt_now - timedelta(days=1)).strftime('%d.%m.%Y')))
month_days = monthrange(date.today().year, date.today().month)
print("Месяц назад было - {}".format((dt_now - timedelta(days=month_days[1])).strftime('%d.%m.%Y')))


date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print(type(date_dt))
