
#mem

#import win32process

def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)

a = sum2(3)
print(a)



'''
zhan 

dui lie

'''
import collections

queue = collections.deque()
print(queue)

queue.append('a')
print(queue)

queue.append('b')
print(queue)

queue.append('c')
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)





