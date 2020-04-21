#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
想用锁的话，先lock 然后 release


'''

import time, random
import threading

lock = threading.Lock()
list = [0] * 10


def p1():
    #获取线程锁， 如果已经上锁，则等待锁的释放
    lock.acquire()  #阻塞
    for i in range(len(list)):
        list[i] = i
        time.sleep(0.1)
    #释放锁
    lock.release()

def p2():
    lock.acquire()
    for i in range(len(list)):
        print(list[i])
        time.sleep(0.1)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=p1)
    t2 = threading.Thread(target=p2)
    t1.start()
    t2.start()


