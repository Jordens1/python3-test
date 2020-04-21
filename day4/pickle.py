import sys,time,os,copy



try :
    print(1 / 0)
except ZeroDivisionError as e :
    print('mirror')

finally:
    print('must me ')


def func(num, div):

    assert (div != 0), '####div not 0 '
    return num /div

print(func(10, 0))

path = '/root/PycharmProjects/darnell/venv/python3test/day3/b.txt'
with open(path, 'r', encoding='utf-8') as f :
    str1 = f.read(10)
    print(str1)
    lines = f.readlines(30)
    print(lines)


import pickle


path2 = '/root/PycharmProjects/darnell/venv/python3test/day4/r.txt'
mylist = [1, 3, 4, 56, 'sunck is a good man ']

#with open(path2, 'r', encoding='utf-8') as f :
