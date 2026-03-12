import os
import sys

from dateutil.parser import parse

sys.path.insert(0, os.path.abspath(".."))
from python_calendar import Calendar

date_from = parse('2023-08-23')
date_to = parse('2024-08-23')
calendar = Calendar.get(date_from, date_to)

print("\nYears : ")
for y in calendar.years:
    print(y)

print("\nMonths : ")
for m in calendar.months:
    print(m)

print("\nWeeks : ")
for w in calendar.weeks:
    print(w)

print("\nDays : ")
for d in calendar.days:
    print(d)