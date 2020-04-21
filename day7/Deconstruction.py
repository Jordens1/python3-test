
class Person(object):
    age = 19
    name = 'haohao'
    heigt = 180
    long = 8
    def sing(self, songname):
        print('i can sing ' + songname)
    def jump(self):
        print('i can jump !')
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

#最后结束的时候会执行
    def __del__(self):
        print('this is deconstruction')


per1 = Person('cxk', 12, 130, 6)
per1.say()


# del per1
#
print(per1.age)

def func():
    per2 = Person('aa', 2, 3, 3)

func()



# while 1:
#     pass





























