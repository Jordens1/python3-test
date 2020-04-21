#/usr/bin/env python
# _*_ coding:utf-8 _*_

from multiprocessing import Process, Queue
import time
'''
进程之间的通信实例
'''
def download(q):
    m = ['a', 'b', 'c', 'd']
    for i in m:
        time.sleep(0.1)
        q.put(i)
def getfile(q):
    while True:
        try:
            print(q.get(timeout = 1))
        except:
            break

if __name__ == '__main__':
    q = Queue(2)
    p1 = Process(target=download, args=(q, ))
    p2 = Process(target=getfile, args=(q, ))
    p1.start()
    #如果不等待的话，进程结束了之后就会回收参数，那p2就得不到数据了

    p2.start()
    p1.join()
    p2.join()
    print('over')

















