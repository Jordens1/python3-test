#！/usr/bin/env python
# _*_ coding:utf-8 _*_

def outer(arg):   # arg = echo()
    def inner():
        print("*" * 20)
        arg()     # echo 原函数
        print("*" * 20)
    return inner

# @outer #
# def echo():
#     print('欢迎来到')
# echo()

def echo():
    print('欢迎来到')
echo = outer(echo)
echo()


li = ["hello","world", 'len', 'network']

for idx, item in enumerate(li):
    print(idx, item)


for idx, item in enumerate(li, 10):
    print(idx, item)










