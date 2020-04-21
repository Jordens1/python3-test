import time

'''
UTC


DST

c = time.time()   b =time.localtime()   z = time.strftime('%Y-%m-%d %H:%M:%S', b)  z = time.strftime('%Y-%m-%d %H:%M:%S')
'''




c = time.time()
print(c)

# print(time.gmtime())
# print(time.gmtime(c))

b =time.localtime(c)
print(b)


m = time.mktime(b)
print(m)


s = time.asctime(b)
print(s)

p = time.ctime(c)
print(p)


z = time.strftime('%Y-%m-%d %H:%M:%S', b)
print(z, type(z))


ti = time.perf_counter()
time.sleep(1)

#ti = time.clock()
# print(ti)

ti2= time.perf_counter()
print(ti2)




