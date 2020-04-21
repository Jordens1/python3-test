#/usr/bin/env python
# _*_ coding:utf-8 _*_
import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt

l1 = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3, 4]
# s1 = pd.Series(l1)
# print(s1)
# s2 = pd.Series(l2, index = l1)  #index自定义索引
# print(s2)
# print(s2.index, s2.values)
#
d1 = {"a":1, 'b':"2"}
# print(pd.Series(d1))


df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
print(df1)
df2  = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C']])
print(df2)

df3  = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C']], columns=['大', '小'], index=['一', '二', '三'])
print(df3)

d2 = {'xiao':[1, 2, 3], 'da':[4, 5, 6]}
df4 = pd.DataFrame(d2)
print(df4)
print(df4.values)







