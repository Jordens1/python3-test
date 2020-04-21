import calendar

print(calendar.__file__)
print(calendar.month(2019, 9))

print(calendar.calendar(2019))
#是否是闰年
print(calendar.isleap(2019))

#这个月空了几天开始的   总共有多少天
print(calendar.monthrange(2019,9))
#每一周对应的日子
print(calendar.monthcalendar(2019, 9))





















