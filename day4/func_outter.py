import os,sys
import outter


def arg_two(comd):
    print(os.system(comd))
    print('ni hao ')


arg = outter.func(arg_two('ls'),1,'ls')


s = outter.data('ls')(arg_two)                #
s()

