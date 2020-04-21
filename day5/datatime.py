import datetime, calendar, time

'''
datetime
timedelta


tginfo
time
date
'''
d1 = datetime.datetime.now()
print(d1, type(d1))

d2 = datetime.datetime(2000, 10, 2, 12, 23, 34, 34567)
print(d2)

d3 = d1.strftime('%Y-%m-%d %X')
print(d3, type(d3))

d4 = datetime.datetime.strptime(d3, '%Y-%m-%d %X')
print(d4, type(d4))



d5 = datetime.datetime(2000, 10, 2, 12, 23, 34, 34567)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7 , type(d7), d7.days, d7.seconds)
print(time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time())))






