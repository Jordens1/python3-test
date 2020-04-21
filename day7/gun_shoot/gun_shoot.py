from person import Person
from gun import Gun
from bulletBox import BulletBox

#one by one object    so you can use a func like a .

bulletBox = BulletBox(5)

gun1 = Gun(bulletBox)

per = Person(gun1)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fillBullet(5)

per.fire()
per.fire()
per.fire()
per.fire()


