#！/usr/bin/env python
# _*_ coding:utf-8 _*_
def func():
    num = 0
    def inner():
        nonlocal num
        num += 1
        return num
    return inner

c = func()
c()
c()
print(c())