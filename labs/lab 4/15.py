from datetime import datetime, timedelta, timezone
import re
import math

def parse_datetime(s):
    date_part, tz_part = s.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    m = re.match(r'UTC([+-])(\d+):(\d+)', tz_part)
    sign = 1 if m.group(1) == '+' else -1
    hours = int(m.group(2))
    minutes = int(m.group(3))
    tz = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=tz)

def next_birthday(birth, current):
    year = current.year
    month = birth.month
    day = birth.day
    while True:
        try:
            bd = datetime(year, month, day, tzinfo=birth.tzinfo)
        except ValueError:
            bd = datetime(year, 2, 28, tzinfo=birth.tzinfo)
        if bd.astimezone(timezone.utc) >= current.astimezone(timezone.utc):
            break
        year += 1
    delta_seconds = (bd.astimezone(timezone.utc) - current.astimezone(timezone.utc)).total_seconds()
    return max(0, math.ceil(delta_seconds / 86400))

birth = parse_datetime(input())
current = parse_datetime(input())
print(next_birthday(birth, current))