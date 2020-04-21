#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
每次创建一个对象就需要分配一个地址空间， 浪费内存


'''

class Person:
    #私有化
    __instance = None

    #重写 __new__
    def __new__(cls, *args, **kwargs):
        # print('cls: ', cls.__instance)
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)          #借助object的__new__创建空间并且赋值
            return cls.__instance
        else:
            return cls.__instance



p1 = Person()
p2 = Person()
#变成了同一个地址
print(p1)
print(p2)

