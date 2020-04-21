
from time import sleep

def progress(percent = 0, width =30):
    left_num = width * percent // 100
    right_num = width - left_num
    print('\r[','#' * left_num, ' ' * right_num,']',f'{percent:.0f}%',sep = '', end  = '', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)
print('\n')


# print('\r[','#' * left, ' ' * right, ']',
#           f'{percent:.0f}%',
#           sep = '', end  = '', flush=True)

import os
a = os.getcwd()
print(os.path.abspath(a))
#os.rename('duixinag.py', 'loading.py')

import json

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(json.dumps(my_mapping, indent = 4, sort_keys=True))








