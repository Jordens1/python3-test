import sys
import time
import random


# print('shufu jiu ')

f = open('a.txt', mode='a+', encoding='utf8')
wei = f.tell()
print(wei)
data = f.read()
print(data)

f.seek(6)
print(f.tell())
print(f.readline())
print(f.tell())
print(f.read())

# print(f.__iter__().__next__())

d4 = f.write('shideba\n')
print(d4, type(d4))
print(f.read())
f.flush()
print(f.read())
print(f.tell())
d = f.mode
print(f.tell())
e = f.name
c = f.closed
print(c, d, e)
print(f.tell())
print(f.readline())

f.close()

with open('a.txt', 'r') as f1 :
    c = f1.readline()
    c2 = f1.tell()
    print(c)
    print(c2)
    print(f1.closed)
    # pos = f1.seek(3, 21)
    print(pos)
    a = f1.tell()
    print(a)
print(f1.closed)

















