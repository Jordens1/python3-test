#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
私有化需要 get set    这样可以不让人直接访问，还可以增加一些判断条件之类的  变成了这样 _Stud__score， dir（）可以看出来

装饰器：上面的升级版 更好用

'''
class Stud:
    def __init__(self, name , age):
        self.name = name
        self.age = age
        self.__score = 45

    def __str__(self):
        return '名字：{}, 年龄：{}, 分数：{}'.format(self.name, self.age, self.__score)

    # def set(self, score):
    #     if  score > 30:
    #         self.__score = score
    # def get(self):
    #     print(self.__score)
    @property
    def score(self):    #  get 的替代
        return self.__score
    @score.setter                  #set 的替代
    def score(self, gei):
        self.__score = gei


A = Stud('xiaoming', 12)
print(A)

# A.set(34)
# A.get()
# print(dir(A))

print(A.score)
A.score = 100
print(A.score)




