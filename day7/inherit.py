
class Person(object):
    def __init__(self, name, age, height, long):
        self.name = name
        self.age = age
        self.heigt = height
        self.long = long
    def jump(self):
        print('i can jump !')

class Student(Person):
    def __init__(self, name, age, height, long, stuId):
        #from father
        super(Student, self).__init__(name, age, height, long)
        #super().__init__(name, age, height, long)
        #from myself
        self.stuId = stuId




stu = Student('tom', 3, 4, 6, 88)

print(stu.name, stu.long, stu.stuId)
stu.jump()


