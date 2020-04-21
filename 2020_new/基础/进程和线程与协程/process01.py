#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
linux: os.fork()

windows：Process()
'''
from multiprocessing import Process
import os, time


def task1(s):
    time.sleep(s)
    while True:
        print( os.getppid() )
        print('1')
def task2(s):
    time.sleep(s)
    while True:
        print( os.getppid() )
        print('2')

if __name__ == '__main__':
    print( os.getpid() )
    #这个py文件运行已经是主进程了， 子进程的创建可以有name， 参数（可迭代的对象）
    p1 = Process(target=task1, name='我是1', args=(2, ))
    p1.name
    p1.start()
    p2 = Process(target=task2, name='我是2', args=(1, ))
    #开始进程
    p2.start()
    p2.name
    num = 1
    while True:
        time.sleep(0.3)
        num += 1
        if num > 10000:
            #终止进程
            p1.terminate()
            p2.terminate()
            print(num)












