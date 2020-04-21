#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
https://blog.csdn.net/ll641058431/article/details/80173660

多继承的顺序 ，广度优先， 从左至右           python3的环境   经典类==新式类
python2 新式类 深度优先

'''

class Base:
    print('base' * 10)

class A(Base):
    print('A' * 10)

class B(Base):
    print('B' * 10)

class C(A, B):
    pass

c = C()

#查看调用的顺序
import inspect
print(inspect.getmro(C))
#或者另外的一种方法
print(C.__mro__)










