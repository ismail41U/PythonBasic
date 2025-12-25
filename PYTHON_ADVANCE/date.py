
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

now_str = now.strftime("%Y")
print("Formatted date and time:", now_str)
now_str = now.strftime("%m")
print("Formatted date and time:", now_str)
now_str = now.strftime("%d")
print("Formatted date and time:", now_str)
now_str = now.strftime("%H")
print("Formatted date and time:", now_str)
now_str = now.strftime("%M")
print("Formatted date and time:", now_str)
now_str = now.strftime("%S")
print("Formatted date and time:", now_str)
now_str = now.strftime("%X")
print("Formatted date and time:", now_str)
now_str = now.strftime("%x")    
print("Formatted date and time:", now_str)
now_str = now.strftime("%c")
print("Formatted date and time:", now_str)
now_str = now.strftime("%A")
print("Formatted date and time:", now_str)
now_str = now.strftime("%a")
print("Formatted date and time:", now_str)
now_str = now.strftime("%B")
print("Formatted date and time:", now_str)

print("-------------------------------------------------")

t = '22 November 1979 hour 21:30:00'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(result)

birthday = datetime(1980, 1, 24, 21, 30, 0)
print(birthday)

result = result.timestamp() # milliseconds since epoch
print(result)
result = datetime.fromtimestamp(result) # convert milliseconds since epoch to date
print(result)
result = datetime.fromtimestamp(0) # epoch time
print(result)

print("-------------------------------------------------")

from datetime import timedelta

today = datetime.now()
print("Today:", today)
tomorrow = today + timedelta(days=1)
print("Tomorrow:", tomorrow)
yesterday = today - timedelta(days=1)
print("Yesterday:", yesterday)

print("-------------------------------------------------")

def days_between(date1, date2):
    delta = date2 - date1
    return abs(delta.days)
date1 = datetime(2020, 5, 17)
date2 = datetime(2021, 6, 18)
print("Days between:", days_between(date1, date2))

print("-------------------------------------------------")

from datetime import date
today = date.today()
print("Today's date:", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
date_str = today.strftime("%Y-%m-%d")
print("Formatted date:", date_str)
date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
print("Date object:", date_obj)

print("-------------------------------------------------")

from datetime import time
t = time(14, 30, 0)
print("Time object:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
time_str = t.strftime("%H:%M:%S")
print("Formatted time:", time_str)

print("-------------------------------------------------")

from datetime import timezone
utc_now = datetime.now(timezone.utc)
print("Current UTC date and time:", utc_now)
local_now = utc_now.astimezone()
print("Local date and time:", local_now)
print("UTC Offset:", local_now.utcoffset())
print("Timezone name:", local_now.tzname())
print("Is DST:", bool(local_now.dst()))
print("ISO format:", local_now.isoformat())

print("-------------------------------------------------")





