class Person(object):
    age = 19
    name = 'haohao'
    heigt = 180
    long = 0

    def jump(self):
        print('i can jump !')
        print(self.__long)
        print("#" * 10)


    def say(self):
        print('my name is %s, my age is %d, my height is %d, my long is %d cm'
              % (self.name, self.age, self.heigt, self.long))

    def __init__(self, name, age, height, long):
        self.name = name
        self.age = age
        self.heigt = height

#can not use/change  outside    just use inside  ##__long ===>  _Person__money   私有
        self.__long = long

#if you want to update it , you should create a func in side   想要更新一个私有的属性，需要写一个函数来对它进行操作  在外部无法进行传参

    def setLong(self, long):
        if long < 10:
            long = 4
        self.__long = long

    def getLong(self):
        return self.__long


per1 = Person('cxk', 12, 130, 6)

per1.say()
print(per1.long)

#per1.__long

per1.jump()

per1.setLong(9)
print(per1.getLong())






























