from datetime import datetime, timedelta

today = datetime.today().date()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(today,tomorrow, yesterday)

date1 = datetime(2025, 5, 30)
date2 = datetime(2025, 12, 30)
print(date2 - date1)
