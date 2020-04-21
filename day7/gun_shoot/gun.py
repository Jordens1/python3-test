#import bulletBox

class Gun(object):
    def __init__(self, buttlebox):
        self.buttlebox = buttlebox

    def shoot(self):
        if self.buttlebox.count == 0:
            print('no bulletCount')
        else :
            self.buttlebox.count -= 1
            print('%d left' % self.buttlebox.count)