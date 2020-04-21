#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
封装  继承  多态(基于继承的，判读是否同属一个大的类)


'''
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pad(self, pet):
        # 判断是不是Pet这个类的对象或者是子类的对象
        if isinstance(pet, Pet):
            print("pet" + self.name, 'xihuan:', pet.padNmae)
            print("pet" + self.name, 'xihuan:', pet.role)
        else:
            print('不是宠物,不要')

class Pet:
    def __init__(self, padName, age):
        self.padNmae = padName
        self.age = age

    def show(self, pet):
        print('')

class Cat(Pet):
    role = '猫'
    def __init__(self, padName, age):
        self.padNmae = padName
        self.age = age

    def catch(self):
        print(self.padNmae + "cat" + self.age)

class Dog:
    role = '狗'
    def __init__(self, padName, age):
        self.padNmae = padName
        self.age = age

    def watch(self):
        print(self.padNmae + "dog" + self.age)

c = Cat('小花', 12)
d = Dog('小黑', 21)
per = Person('xiaoming')
per.feed_pad(c)
per.feed_pad(d)