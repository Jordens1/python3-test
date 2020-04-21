# def funx():
#     x=5
#     print(x,'##')
#     def funy():  # 内部函数中只能对外部函数的局部变量进行访问，不能修改
#         #读取了一次之后在内部函数里就有了值,不需要再次从外部函数读取
#         nonlocal x  # 如果需要修改则需要用到 nonlocal关键字
#
#         x+=1
#         return x
#     return funy
#
# a = funx()
# print(a())
# print(a())
# print(a())
# print(a())


def func(arg,x,comd):
    def inner():
        if x == 1:
            print("#" * 10)
            arg(comd)
            print("#" * 10)
        else :
            print('wrong')
    return inner



# import os
# print(os.)

def data(*args):
    def outter(arg_two):
        def inner():
            print(args)
            print("#" * 10)
            arg_two(args[0])
            print("#" * 10)
        return inner
    return outter


