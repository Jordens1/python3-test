#/usr/bin/env python
# _*_ coding:utf-8 _*_

#排列的一个库
import itertools
#拆包，装包
from time import sleep

print(*[1, 3, 4, 5])

list = [1, 2, 3, 4, 4, 5 ]
a, *_, b = list
# assert isinstance(a)
print( a )
print(b)
print(_)

#sublime安装配置    前端：Hbuilder、WS（jetbrains）

#解包语法
def a(name, age, hig):
    print(name, age, hig)
dic = {'name':'xishi', 'age': 18, 'hig':189}
a(**dic)














