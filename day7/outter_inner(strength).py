
import datetime,time
from functools import wraps

def test(timed = 0):
    def outter(func):
        @wraps(func)          #can have his really name
        def inner(a, b):
            print(datetime.datetime.now())
            func(a, b)
            if timed:
                time.sleep(2)
            print(datetime.datetime.now())
        return inner
    return outter

#the () is for test()
@test(' ')
def my(name, age):
    print(f'{name}{age}')

print(my.__name__)

#my('nihao', 18)

def func():
    print(f'{name}{age}')

print(func.__name__)


class Test():
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print(datetime.datetime.now())
        self.func(a, b)
        print(datetime.datetime.now())

@Test
def my(name, age):
    print(f'{name}{age}')

my('xiao ming', 10)


