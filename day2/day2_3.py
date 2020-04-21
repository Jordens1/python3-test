import sys
import time
import random


dict1 = {}
print(type(dict1))

dict1['one'] = '1 - hello'
print(dict1)

tinydict = {'name': 'hello','code':1, 'site': 'nihao'}

print(tinydict.keys())
print(tinydict.values())

dict2 = {x: x**2 for x in (2, 3, 4, 5, 9)}
print(dict2)

dict3 = {'kunkun': 'nan', 'haohao': 'nannan'}
print(dict3)

print(dict3['haohao'])

del dict3['kunkun']
print(dict3, type(dict3))

b = str(dict3)
print(b, type(b))



dict4 = {'Name': 'Baidu', 'Age': 7, 'Class': 'First'}

dict5 = dict4.copy()
print(dict5)


lst2 = (3, 5, 6)
dict6 = dict.fromkeys([lst2, 10])
print(dict6)

print(dict6.get(100, 'bushi'))

print(dict4)
g = dict4.popitem()
print(g)

v = [x*5 for x in range(2, 10, 2)]
print(v)













