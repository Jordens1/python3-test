#！/usr/bin/env python
# _*_ coding:utf-8 _*_


a = map(str, [1, 2, 3, 4, 5])
print(list(a))
c = list(a)
#print(type(c))

from functools import reduce
def MySum(a, b):
    c = a + b
    return c

sum = reduce(MySum, (1, 3, 5, 5, 6, 9))
print(sum)
#reduce(f, (a, b, c, d))


def str2imt(str):
    def fc(x, y):
        return x * 10 + y
    def fs(str):
        #return {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}[chr]
        return map(int, str)

    return reduce(fc, list(fs(str)))

c = str2imt(["3", "4", "4", "9", "8"])
print(c)


#index的作用
# c = "444.897"
# n = c.index('.')
# print(n)

def is_odd(n):
    return n % 2 == 1

tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)








