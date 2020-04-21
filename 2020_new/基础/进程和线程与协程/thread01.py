#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
线程的运行过程： 准备--就绪--运行--         --结束
                              --阻塞--运行--

在阻塞的时候会把执行权让给别的线程

'''
import time
import threading

def download(n):
    m = ['a', 'b', 'c', 'd']
    for i in m:
        print(i)
        time.sleep(n)

def listen(n1):
    m = ['1', '2', '3', '4']
    for i in m:
        print(i)
        time.sleep(n1)
if __name__ == '__main__':
    n, n1= [1, 1.5]
    t1 = threading.Thread(target=download, args=(n, ))
    t2 = threading.Thread(target=listen, args=(n1, ))
    t1.start()
    t2.start()
    print('++over')










