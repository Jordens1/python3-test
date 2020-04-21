#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
在原来的Process里无法调用进程的方法比如；terminate, name

'''
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    #重写run
    def run(self):
        print('这是进程的名字： ', self.name)


if __name__ == '__main__':
    while True:
        p1 = MyProcess('ying')
        p1.start()
        p2 = MyProcess('wang')
        p2.start()














