import itertools


#permutation
mylist = list(itertools.permutations([1, 2, 3, 4], 3))

print(mylist , len(mylist))


#combination
mylist1 = list(itertools.combinations([1, 2, 3, 4], 3))

print(mylist1 , len(mylist1))


#permutation and combination
# mylist3 = list(itertools.product([1, 2, 3, 4, 5, 6, 7, 8], repeat=4))
#
# print(len(mylist3))
#


passwd = ("".join(x) for x in itertools.product("0987654321", repeat=3))

# print(next(passwd))
# print(next(passwd))
# print(next(passwd))
# print(next(passwd))
# print(next(passwd))

while True:
    import time
    try :
        time.sleep(0.5)
        str = next(passwd)
        #print(str)
    except StopIteration as e :
        break













