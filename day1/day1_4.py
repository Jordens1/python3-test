import math
import random
import sys

lst = ['bilili', 'bai', 'good', ['job', 'yes', 9]]
print(lst , type(lst))
del lst[1]
print(lst)

a = len(lst)
print(a)

biao = ['aa', 'cc', 890]

print(lst + biao)

print(lst * 4)


for i in lst:
    print(i)

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst1[2:5])
lst1[2:4] = []
print(lst1)

a = (1, 3, 4, 5, 6)
print(type(a))
d = list(a)
print(d, type(d))

e = [1, 3, 4, 5, 2, 2, 4, 'r', 't', 'po']
e2 = [4, 5, 'i']
e.append('die')
print(e)
c1 = e.count(1)
print(c1)
e.extend(e2)
print(e)
e.insert(9, 'www')
print(e)
f = e.pop(-2)
print(e, f)

lst1.reverse()
print(lst1)
lst1.sort()
print(lst1)

lst2 = lst1.copy()
print(lst2)

lst3 = [3, 4, [4, 6, 9]]
lst4 = lst3.copy()

lst3[-1][-1] = 't'
lst3[1] = 'u'
print(lst3)
print(lst4)
