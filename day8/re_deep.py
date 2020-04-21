import re


str1 = 'sunck     is a good man, sunck     is a nice man, sunck     is a very man'

print(re.split(r' +', str1))

d = re.finditer(r'(sunck)', str1)
while True:
    try:
        l = next(d)
        print(l)
    except StopIteration as e:
        break



str2 = 'sunck     is a good man, sunck     is a nice man, sunck     is a very man'

print(re.sub(r'sunck', 'xishi', str2))
print(type(re.sub(r'sunck', 'xishi', str2)))
print(re.subn(r'sunck', 'xishi', str2))
print(type(re.subn(r'sunck', 'xishi', str2)))




str3 = '098-34567890'

b = re.match(r'((?P<head>\d{3})-(?P<back>\d{8}))', str3)
print(b.group(0))
print(b.group(1))
print(b.group(2))
print(b.group(3))
print(b.groupdict(0))
print(b.group('head'))
print(b.groups())


pat = r'((?P<head>\d{3})-(?P<back>\d{8}))'
re_phone = re.compile(pat)
re_phone.match(str3)























