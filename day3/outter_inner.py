import time,copy,sys,os,_functools


#functools.partial

#print(os.__doc__)

#print(vars(os))

#help(sys)

#除数和余数
# print(divmod(39, 4))
#
# print(all([6, 7, 8, 5]))

def outer(func):
    def inner():
        print("************")

        func()
    return inner

@outer
def func():
    print('hello word')

#func()

a = range(1, 19)
print(type(a))
print(a)
print(a[1], a[0])

def foo():
    print('from foo')
    func1()

def func1():
    print('from func1')

foo()
print(foo())

#枚举,前面的是下标
l = [1,2,3,4]
for v in enumerate(l):
    print(v)
# 观察规律

l = [1,2,3,4]
for v in enumerate(l,100):
    print(v)

def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(1,2,3)
func1(k1=1,k2=2)
func1(1,2,3,k1='a',k2='b')
