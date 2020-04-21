#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
如果两个线程分别的占用了一部分的资源并且同时的等待着对方的资源，就会造成死锁， 程序就不响应了

解决办法：
1、重构代码
2、加入 timeout
'''
from threading import Thread, Lock
import time

lock1 = Lock()
lock2 = Lock()

class MyThread1(Thread):
    def run(self):
        if lock1.acquire():    #acquire 返回的是bool类型的值
            print(self.name + '获取了1锁')
            time.sleep(0.2)
            #获取了1之后转让执行权， 之后2被Mythred2获取则无法进行下面的从而阻塞在这里
            if lock2.acquire():
                print(self.name + '获取了2锁')

class MyThread2(Thread):
    def run(self):
        if lock2.acquire():
            print(self.name + '获取了2锁')
            time.sleep(0.2)
            if lock1.acquire():
                print(self.name + '获取了1锁')

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()














