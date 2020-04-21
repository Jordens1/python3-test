#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
驼峰命名，object可以省略
魔术方法 __名字__

类方法 @classmethod  :类的方法，不依赖于self这个实体

__shuxing   私有化

@staticmethod   静态方法


__init__   在初始化对象时触发

__new__    在实例化是触发， 想当于就是实例化对象时申请内存空间，return 返回一个内存地址

__call__              #把对象当函数用

__del__             # del 删除对于这个地址的引用    再没有人引用这个地址就默认执行__del__
python解释器再执行完之后会回收使用的地址空间，这时就会触发__del__

__str__    #想在打印对象名的时候更加的具体化，体现更多的信息
'''

class Dog:
    __age = 18    #类属性
    def __init__(self, name):
        self.name = name   #name是self的，不是类的

    def run(self):
        print("pao")
        self.dance()    #类中调用方法也是依赖于self调用的
    def dance(self):
        print("dance")

    @classmethod
    def test(cls):   #传的是类，里面只能使用本身自带的属性（类属性、类方法）
        print('a')
    @classmethod
    def show_age(cls):
        cls.__age=20
        print(cls.__age)
    @staticmethod    #静态方法  只能使用类的东西 使用同类方法
    def test():
        print('#' * 10)

    def __new__(cls, *args, **kwargs):
        print("#" * 9)
        # 返回的是地址
        return object.__new__(cls)

    # 把对象当函数用
    def __call__(self, *args, **kwargs):
        print('call###############')

    # del 删除对于这个地址的引用    再没有人引用这个地址就默认执行__del__
    def __del__(self):
        print('del############')

    # 想在打印对象名的时候更加的具体化，体现更多的信息
    def __str__(self):
        return '名字是：' + self.name

bai = Dog('bai')

bai.test()
Dog.test()
# print(Dog.age)
bai.show_age()

bai()

bai2 = bai
bai3 = bai
import sys
print(sys.getrefcount(bai))   #引用的个数，包括这次引用

del bai2
print(sys.getrefcount(bai))

print(bai)