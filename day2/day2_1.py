import math
import random
import sys
import time
tup = (50)
tup1 = (50,)
tup3 = 'a', 'v', 'u'

print(type(tup), type(tup1), type(tup3))

tuple1 = ( 'abcd', 786 , 2.23, 'hello', 70.2  )
tinytuple = (123, 'hello')
print (tuple1)             # 输出完整元组
print (tuple1[0])          # 输出元组的第一个元素
print (tuple1[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple1[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)      # 输出两次元组
print (tuple1 + tinytuple) # 连接元组

tuple2 = 'ni', 'shi', 'shei'
tuple3 = tuple1 + tuple2
print(tuple3)

# del tuple1
# print(tuple1)
tuple11 = (2, 3, 5, 7, 9)
tuple12 = ('v', 'v', 'v', 't')
print(max(tuple11))
v = min(tuple12)
print(v)
v1 = len(tuple11)
print(v1)

v3 = list(tuple11)
print(v3)
v4 = tuple(v3)
print(v4)


student = {'tom', 'alice', 'jack', 'head'}
print(student, type(student))

student1 =set('dgmhjkbu')
student2 = set('vjkagvuobt')
print(student1, student2)

print(student1 - student2)
print(student1 | student2)
print(student1 & student2)
print(student1 ^ student2)

student1 = {x for x in 'zxcvbnm' if x not in 'zxcv'}
print(student1)

thisset = set(("Google", "Baidu", "Taobao"))
print(thisset)

thisset.add("Facebook")
print(thisset)

thisset.update({'ds', 5}, ('c', 5), [5, 6])
print(thisset)

thisset.remove('ds')
print(thisset)
# thisset.remove('ds')
# print(thisset)
pass
thisset.discard("ds")
print(thisset)
time.sleep(5)
thisset.pop()
print(thisset)


