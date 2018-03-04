import datetime as dt

d = dt.date(*[int(i) for i in input().split()]) + dt.timedelta(int(input()))
print(d.year, d.month, d.day)
