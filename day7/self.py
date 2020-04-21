
# self is not a keyword  (deaulft)
#self is yourself
#self.__class__    ==== Person      you can use this to create a object

class Person(object):
    #相当于是位置参数
    age = 19
    name = 'haohao'
    heigt = 180
    long = 8
    def sing(self, songname):
        print('i can sing ' + songname)
    #self.__class__相当于是这个类
    def jump(self):
        print('i can jump !')
        p = self.__class__('tt', 43, 54, 6)
        p.say()

    def rap(self):
        print('i can rap')

    def say(self):
        print('my name is %s, my age is %d, my height is %d, my long is %d cm'
               %(self.name, self.age, self.heigt, self.long))


    def __init__(self, name, age, height, long):
        self.name = name
        self.age = age
        self.heigt = height
        self.long = long

per1 = Person('cxk', 12, 130, 6)
per1.say()

per1.jump()

per2 = Person('cxk2', 12, 130, 6)
per2.say()

per1.sing('nihao ')





















