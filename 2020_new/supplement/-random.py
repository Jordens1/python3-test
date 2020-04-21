#/usr/bin/env python
# _*_ coding:utf-8 _*_


'''
标准库的东西， print() set()  bin()  hex() oct() isinstance()

'''
import random
c = random.random()
print(c)  #产生小数
#1 3 5
c = random.randrange(1, 10, 2)   #1--10 步长2
print(c)
#取1-10
c = random.randint(1, 10)
#随机取值
list = ['a', 'b', 'c', 'd']
c = random.choice(list)
print(c)
#打乱列表
random.shuffle(list)
print(list)


#产生一个验证码，需要数字、大小写
def ma():
    code = ''
    for i in range(4):
        num = str(random.randint(0, 9))
        xiao = chr(random.randint(65, 90))  #chr 将数字转换为字母    ord   将字母转换为数字      汉字也可以
        da  = chr(random.randint(97, 122))
        list = [num, xiao, da]
        one = random.choice(list)
        code +=one

    return code

c = ma()



















