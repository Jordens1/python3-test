#！/usr/bin/env python
# _*_ coding:utf-8 _*_

#开枪射击子弹
class Person(object):
    def __init__(self, gun):
        self.gun = gun
    def shut(self):
        self.gun.shut()
    def add(self, count):
        self.gun.add(count)


class Gun(object):
    def __init__(self, bullet_box):
        self.bullet_box = bullet_box
    def shut(self):
        if  self.bullet_box.count > 0:
            self.bullet_box.count -= 1
            print("子弹还剩%d" % (self.bullet_box.count))
        else:
            print("子弹不够了，请加弹")
    def add(self, add_count):
        self.bullet_box.count = add_count

class BulletBox(object):
    def __init__(self, count):
        self.count = count

b = BulletBox(4)
g = Gun(b)
p = Person(g)
p.shut()
p.shut()
p.shut()
p.shut()
p.add(3)
p.shut()
p.shut()