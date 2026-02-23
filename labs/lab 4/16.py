from datetime import datetime, timedelta, timezone
import re

def parse_datetime(s):
    dt_part, tz_part = s.rsplit(' ', 1)
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    m = re.match(r'UTC([+-])(\d+):(\d+)', tz_part)
    sign = 1 if m.group(1) == '+' else -1
    hours = int(m.group(2))
    minutes = int(m.group(3))
    tz = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=tz)

start = parse_datetime(input())
end = parse_datetime(input())

duration_seconds = int((end.astimezone(timezone.utc) - start.astimezone(timezone.utc)).total_seconds())
print(duration_seconds)