import math
import random
import sys

# alpha1 = 'ni hao ma ?'
# alpha2 = '\nwo bu hao !'
#
# print(alpha1 + alpha2)
#
# print(alpha1[1:])

alpha1 = 'ni hao ma ?'
alpha2 = '\nwo bu hao !'

n = 0
for i in alpha1:
    if i == 'm':
        print(n, alpha1[n])
    n +=1


if 'a' in alpha1:
    print('you right')


print('my name is %s, age is %d' % ('darnell', 19))



print('the ascii is %c' % 78)


'''
str = "this is string example....wow!!!";

sub = "i";
print ("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow";
print ("str.count(sub) : ", str.count(sub))

'''

print('welocme to %12.8c' % 77)

print(f'welocme\v to %12.8c' % 77)

print('%-10.3d' % 99)

print('%+d' % -99)


str = ' odd is you ma '
print(str.capitalize())
print(str.center(30,'#'))
print(str.count('y', 0, 9))



intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str1 = "this is string example....wow!!!"
print (str1.translate(trantab))

code_try = 'such a good boy !'
code_ok = code_try.encode('utf-8')
print(code_ok)
code_try = code_ok.decode('utf-8')
print(code_try)

str_find = 'a beautiful kun standing outside the window'
num = str_find.find('the', 0, len(str_find))
print(num, type(num))

str_find.index('ojbk', 0, len(str_find))









