#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
多个同名的函数，就是覆盖了



'''

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def eat(self):
        print('吃东西')
    def run(self):
        print('跑步')

class Stud(Person):
    def __init__(self, name, age):
        print('111111111')
        super().__init__(name, age)


class Employee(Person):
    def __init__(self, name, age, goods):
        super(Employee, self).__init__(name, age)    #想当于加了一个判断，自己是不是这个Employee
        self.goods = goods                                #还可以拥有自己的属性
    def eat(self):               #重写eat
        super().eat()   #父类的
        print('子类自己的')

stu1 = Stud('xiaohong', 23)
stu1.eat()
emp = Employee('wang', 12, ['yagao', 'yashua'])
print('#' * 10)
emp.eat()
