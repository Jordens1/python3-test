#/usr/bin/env python
# _*_ coding:utf-8 _*_

from multiprocessing import Process, Pool
import time, random
import os
'''
进程池里面满了，就不加了，一直在外面等着有进程结束了才加入进去
    阻塞：一个接一个执行，上一个不结束下一个不执行
    非阻塞：在池子里的进程一起进去了，一起执行着，完成一个补一个
进程消耗大

'''
def task(taskname):
    start = time.time()
    print('开始了{}'.format(taskname))
    time.sleep(random.random() * 2)
    end = time.time()
    # print('shijian', (start - end) + '进程用时：' + os.getpid())
    return start - end

#定义一个回调函数， 一定要有参数，相当于接受上面的return
container = []
def call_func(n):
    container.append(n)

if __name__ == '__main__':
    p = Pool(3)
    t = ['chi', 'he', 'la', 'sa', 'shui', 'xiao', 'ku']
    for i in t:
        #非阻塞式的      注意args是可迭代的
        p.apply_async(task, args=(i, ), callback=call_func)
    #添加任务结束
    p.close()
    #没完成就不能结束主进程
    p.join()
    #最后打印出来
    for i in container:
        print(i)


    # for i in t:
    #     #阻塞式的      注意args是可迭代的
    #     p.apply(task, args=(i, ))
    # p.close()
    # p.join()
    # print('over')







