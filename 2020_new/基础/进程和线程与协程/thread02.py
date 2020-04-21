#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
python解释器在使用线程的时候默认加锁：全局解释器锁GIL（小数据量的时候），大数据量的时候不加

解决线程出现的数据不安全的情况：线程同步（加锁）

进程和线程与协程（占内存）：计算密集型
线程：耗时操作
'''
import threading
n = 0
def jia():
    global n
    for i in range(100000):
        #计算太大的时候，在赋值的时候会被抢占了，导致数据出错
        n += i

def jia1():
    global n
    for i in range( 100000 ):
        n += i

if __name__ == '__main__':
    t1 = threading.Thread(target=jia)
    t2 = threading.Thread(target=jia1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(n)