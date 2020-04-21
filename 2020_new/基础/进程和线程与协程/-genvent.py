#/usr/bin/env python
# _*_ coding:utf-8 _*_


'''
猴子补丁
gevent：在进行耗时的IO操作的时候，会将协程自动的切换，保证充分运行

'''
import time, gevent
from gevent import monkey

monkey.patch_all()
def a():
    i = 0
    while i< 9:
        print('唱第%d首歌'.format(i))
        i += 1
        time.sleep(0.2)

def b():
    j = 0
    while j< 7:
        print('跳第%d只舞'.format(j))
        j += 1
        time.sleep(0.2)

def c():
    k = 0
    while k< 7:
        print('跳第%d只舞'.format(k))
        k += 1
        time.sleep(0.2)



if __name__ == '__main__':
    g1 = gevent(a)
    g2 = gevent(b)
    g3 = gevent(c)

    g1.join()
    g2.join()
    g3.join()
    # gevnent.join_all(g1, g2, g3)










