#/usr/bin/env python
# _*_ coding:utf-8 _*_

from multiprocessing import Queue

'''
进程之间的通信，通过queue进行，先进先出

'''
#队列里面的个数
q = Queue(3)


q.put('aa')
q.put('bb')
q.put('cc')
#个数
print(q.qsize())
#返回真假值，是否满了
if not q.full():
    q.put(1)
else:
    print('full')
    #等待的超时时间
    print(q.get(timeout=2))
    #不等待
    print(q.get_nowait())
    q.put_nowait('dd')











