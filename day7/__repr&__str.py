class Person(object):
    def __init__(self, name, age, height, long):
        self.name = name
        self.age = age
        self.heigt = height
        self.long = long

#foe user    its high privilege
    #输出显示的作用
    def __str__(self):
        return '%s-%d-%d-%d' % (self.name, self.age, self.heigt, self.long)

#for robot
    # def __repr__(self):
    #     return '%s-%d-%d-%d' % (self.name, self.age, self.heigt, self.long)



#when you want to print all the values


per1 = Person('cxk', 12, 130, 6)

print(per1)

































