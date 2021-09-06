import datetime

t1 = datetime.date(2024, 7, 26)
t2 = datetime.date.today()

diff = t1 - t2

print("Today is", t2.strftime("%Y/%m/%d"))
print(diff.days, "days until Paris Olympic")