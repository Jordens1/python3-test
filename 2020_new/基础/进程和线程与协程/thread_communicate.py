#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
线程之间的通信：生产者和消费者

queue模块中：先进先出 Queue、后入先出 LifeQueue、优先级队列 PriorityQueue



'''
import threading
import queue, random, time

def procude(q):
    i= 0
    while i < 10:
        num = random.randint(1, 100)
        q.put(num)
        time.sleep(0.5)
        i += 1
    q.put(None)
    q.task_done()

def consume(q):
    while True:
        item = q.get()
        print(item)
        if item is None:
            break
        time.sleep(1.3)
    q.task_done()

if __name__ == '__main__':
    q = queue.Queue(7)
    arr = []
    #创建生产者
    th = threading.Thread(target= procude, args=(q, ))
    th.start()
    #创建消费者
    th1 = threading.Thread(target= consume, args=(q, ))
    th1.start()

    th.join()
    th1.join()












