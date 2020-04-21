import os

import time
# os.rename('a.txt1', 'a.txt')
#
# time.sleep(3)
# os.rename('a.txt', 'a.txt1')


# os.mkdir('nike')
# time.sleep(3)
# os.remove('nike')

print(os.getcwd())

# os.rmdir('nike')

# os.rename('a.txt1', 'a.txt')


with open('a.txt', encoding='utf8', mode='r+') as f1:
    # data = f1.readlines()
    # print(data)
    # for i in data :
    #     print(i)
    count = 0
    for line in f1:
        print(line)
        if count == 3:
            line =''.join([line.strip(),'end 3'])
        print(line.strip())
        count += 1
        print(count)

a = [4, 3, 5, 8]
b = list(set(a))
print(b)
if len(a) == len(b):
    print('ok')
else :
    print('not ok')



# import time,sys
#
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.1)


with open('a.txt', mode='rb') as f :
    print(f.read())

import copy





