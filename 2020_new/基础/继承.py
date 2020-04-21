#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
is a   以及  has a 的关系

一个类中使用另一个类

系统类型和自定义类型

'''
class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('上网')
    def __str__(self):
        return self.brand + '__' + self.type + '__' +  self.color

class Book:
    def __init__(self, bname, auther, number):
        self.bname = bname
        self.auther = auther
        self.number = number
    def __str__(self):
        return self.bname + '__' + self.auther + '__' + self.number

class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)
    def borrow_bok(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('借了')
            else:
                print('meijie')

#computer就是自定义类            list, dir 就是系统类
    def __str__(self):
        return self.name + "__" + str(self.computer) + "__" + str(self.books)    #强行转换之后就是自动调用对象就调用了__str__, books是列表
    def show_book(self):
        for book in self.books:
            print(book.bname)


com = Computer('mac', 'mac pro', '白色')
boo = Book('盗墓笔记', '南派三叔', '10')
stu = Student('张三', com, boo)
print(stu)
boo1 = Book('gui', 'shu', '9')
stu.show_book()
stu.borrow_bok(boo1)
stu.borrow_bok(boo)







