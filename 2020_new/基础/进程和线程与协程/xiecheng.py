#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
协程(生成器原理)：微线程
耗时操作（网络请求、IO操作）

greenlet：已经实现了完成协程任务，但是需要手动进行操作

'''
import greenlet, time


def a(i):
    while i< 9:
        print('唱第%d首歌'.format(i))
        i += 1
        #g2.switch()
        time.sleep(0.2)

def b(j):
    while j< 7:
        print('跳第%d只舞'.format(j))
        j += 1
        #g3.switch()
        time.sleep(0.2)

def c(k):
    while k< 7:
        print('跳第%d只舞'.format(k))
        k += 1
        #g1.switch()
        time.sleep(0.2)


if __name__ == '__main__':
    g1 = greenlet(a(4))
    g2 = greenlet(b(5))
    g3 = greenlet(c(3))
    # g1.switch()







