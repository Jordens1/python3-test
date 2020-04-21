#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
可迭代的对象：列表 元组 字典 字符串 生成器
迭代器：可以用next 只前进不后退



'''
#判断是否可迭代
from collections.abc import Iterable

items = [1, 2, 3, 4]
f = isinstance(items, Iterable)
print(f)

#生成器通过 iter 变成迭代器
it1 = iter(items)
print(next(it1))







