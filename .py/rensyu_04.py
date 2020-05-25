animals = [{'猫','三毛'},{'犬','コーギー'},{'猫','シャム'},{'犬','ダックス'},{'犬','黒ラブ'}]

d = {}
for k, v in animals:
    if k not in d:
        d[k] = [v]
    else:
        d[k].append(v)
print(d)

import datetime
d1 = datetime.date(2020,5,25)
td = datetime .timedelta(days=100)
d2 = d1 + td
print(d2)

import calendar
print(calendar.month(2020,5))

