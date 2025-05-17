import datetime

now = datetime.datetime.now()
today = datetime.date.today()
print(now)
# print(today)

formatted_date = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted_date)
