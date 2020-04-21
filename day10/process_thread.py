from multiprocessing import Process, Pool
import time, os, random

# def run(str):
#     while True:
#         print('i am a good and %s man' % str)
#         time.sleep(1.2)
#
#
# if __name__ == '__main__':
#
#     p = Process(target=run, args='n')
#     p.start()
#
#
#     while True:
#         print('wo shi ge hao r')
#         time.sleep(1)
#
# print(os.getpid(), os.getppid())
# num  = 100
# def run1():
#
#     print("孙子进程开始...")
#     print("孙子进程结束...%s"%(num))
#
# def run():
#     print("子进程开始...")
#     global num
#     num += 1
#     print(num)
#     p = Process(target=run1)
#     p.start()
#     p.join()
#     print("子进程结束...")
#
# if __name__ == '__main__':
#     print("父进程开始...")
#     p = Process(target=run)
#     p.start()
#     p.join()
#     num += 10
#     print("父进程结束...%d"%(num))

# def func(name):
#     print("子进程%s启动..."%(name))
#     start = time.time()
#     time.sleep(random.choice([1,2,3]))
#     end = time.time()
#     print("子进程%s结束...耗时%.2f"%(name,end - start))
#
# if __name__ == '__main__':
#     print("父进程开始...")
#     pp = Pool(2)
#     for i in range(4):
#         pp.apply_async(func,args=(i,))
#     pp.close()
#     pp.join()
#     print("父进程结束...")


import threading


# def run(num):
#     print("子线程%s开始..."%(threading.current_thread().name))
#     time.sleep(2)
#     print(num)
#     time.sleep(2)
#     # current_thread  返回一个当前线程的实例
#     print("子线程%s结束..."%(threading.current_thread().name))
# if __name__ == '__main__':
#     print("主线程%s启动..."%(threading.current_thread().name))
#     # 创建子线程
#     t = threading.Thread(target = run,args = (1,))
#     t.start()
#     t.join()
#     print("主线程%s结束..."%(threading.current_thread().name))




#
# num = 0
# var = 0
# def run(n):
#     global num
#     for i in range(1000000):
#         num += n
#         num -= n
# def run1(n):
#     global var
#     for i in range(100):
#         var += n
#         var -= n
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run,args=(6,))
#     t2 = threading.Thread(target=run,args=(9,))
#     t3 = threading.Thread(target=run,args=(5,))
#     t3.start()
#     t1.start()
# #     t2.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     print("num = %s"%(num))
#
#
#
# lock = threading.Lock()
# num = 0
#
# def run(n):
#     global num
#     for i in range(1000000):
#         # 加锁  为了确保下面代码只能由一个线程从头到尾的执行
#         # 会阻止多线程的并发执行，所以效率会大大降低
#         """
#         lock.acquire()
#         try:
#             num = num - n
#             num = num + n
#         finally:
#             # 解锁
#             lock.release()
#         """
#         with lock:
#             num = num + n
#             num = num - n
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run,args=(6,))
#     t2 = threading.Thread(target=run,args=(9,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("num = %s"%(num))