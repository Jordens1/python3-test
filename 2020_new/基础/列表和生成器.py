#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
列表推导式： [新列表 for 变量 in 旧列表 if]  以及推导

字典推导式： {value : key for key, vlaue in dic.items()}

生成器： （新列表 for 变量 in 旧列表）    yield 关键字

'''
#1
names = ['xishi', 'xiaoming', 'zhangsan', 'wangwu']
result = [i for i in names if len(i)>5]
print(result)

#2
result = [i.capitalize() for i in names if len(i)>5]
print(result)
#3
result = [ (x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 == 1 ]
print(result)
#4
# list = [(), (), ()]
# [ x[-1] for x in list ]

#5
dic1 = {'sal': 400}
dic2 = {'sal': 700}
dic3 = {'sal': 900}
list3 = [dic1, dic2, dic3]

res3 = [peo['sal']+200 if peo['sal'] > 400 else peo['sal']+300 for peo in list3]
print(res3)

#生成器不占用内存
g = (x*2 for x in range(10))
print(g.__next__())
print(g.__next__())
print(g.__next__())

print(next(g))
print(next(g))
print(next(g))

#斐波那契数列
def num():
    n = 0
    while True:
        n += 1
        yield n     #return n  暂停

g = num()
# print(type(g))
print(next(g))
print(next(g))
print(next(g))

def shulie(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a+b
        n += 1
    return '没有元素了'
res = shulie(5)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
#print(next(res))


#升级
def fanhui():
    a, b = 0, 1
    n = 0
    while n < 3:
        temp = yield b   #这里暂停了并且返回了b   下一次这里开始
        print('temp:', temp)
        for i in range(temp):
            print('------->' ,i)
        a, b = b, a+b
        n += 1
    return '没有元素了'

res = fanhui()
print(res.send(None))   #第一次
print(res.send(3))
print(res.send(4))

#应用  协程
def sing(i):
    while i< 9:
        print('唱第%d首歌'.format(i))
        yield
        i += 1
def dance(j):
    while j< 7:
        print('跳第%d只舞'.format(j))
        yield
        j += 1
g1 = sing(5)
g2 = dance(5)
while True:
    g1.__next__()
    g2.__next__()