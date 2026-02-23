# Date and time operations

#1.
from datetime import date, timedelta
today = date.today()
five_days_ago = today - timedelta(days=5)
print("Today:", today)
print("5 days ago:", five_days_ago)


#2.
from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3.
from datetime import datetime
now = datetime.now()
no_micro = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:", no_micro)


#4.
from datetime import date
d1 = date(2026, 2, 20)
d2 = date(2026, 2, 23)
seconds = abs((d2 - d1).days) * 86400
print(seconds)