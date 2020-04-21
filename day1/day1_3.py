import math
import random
import sys


str1 = 'vlhdfvh'
str2 = '  '
str3 = 'DJGvkfv'
str4 = '65853794'
print(str1.isalnum())
print(str1.isdigit())
print(str1.islower())
print(str4.isnumeric())
print(str2.isspace())

print(str1.lstrip('v'))

print(max(str3), min(str3))

print(str3.replace('v','A',1))


c = str1.split('h', 1)
print(c)

print(str1.swapcase())
print(str1.upper())




























