
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
    #when you use it to create a object , it will work at once   (default)
    def __init__(self, name, age, height, long):
        self.name = name
        self.age = age
        self.heigt = height
        self.long = long


per1 = Person('cxk', 12, 130, 6)
print('######################')

print(per1.name, per1.age, per1.heigt, per1.long)


# per1.name = 'kunkun'
# per1.long = 18
# per1.heigt = 180
# per1.age = 23
#
# print(per1.name, per1.age, per1.heigt, per1.long)
print('##################')
per1.rap()
per1.sing('are you ok ?')

per2 = Person('xx', 12, 23, 4)

print(per2.name, per2.age, per2.heigt, per2.long)









