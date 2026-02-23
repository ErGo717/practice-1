from datetime import datetime, timedelta, timezone
import re

def parse_datetime(s):
    date_part, tz_part = s.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    m = re.match(r'UTC([+-])(\d+):(\d+)', tz_part)
    sign = 1 if m.group(1) == '+' else -1
    hours = int(m.group(2))
    minutes = int(m.group(3))
    tz = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    dt = dt.replace(tzinfo=tz)
    return dt

dt1 = parse_datetime(input())
dt2 = parse_datetime(input())
delta = abs((dt1 - dt2).total_seconds())
days = int(delta // 86400)
print(days)