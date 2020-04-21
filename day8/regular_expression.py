import re


#re.match(pattern, string, flags)

print(re.match('www', 'www.com.nihao'))
print(re.match('www', 'ww.com.nihao'))
print(re.match('www', 'com.www.nihao'))
print(re.match('www', 'WWW.com.nihao'))
print(re.match('www', 'WWW.com.nihao', flags=re.I))

#position
print(re.match('www', 'www.com.nihao').span())

print('#############################')

#re.search(pattern, string, flags)
print(re.search('www', 'com.www.nihao'))


#findall(pattern, string, flags)
print(re.findall('www', 'com.WWW.nihao.www.www', flags = re.I))



print(re.search('[0-9]', 'nihaoa 1wo shi shei ne'))
print(re.search('[\d]', 'nihaoa 1wo shi shei ne'))

print(re.search('[^a-z ]', 'nihaoa 1wo shi shei ne'))
print(re.findall('[^a-z ]', 'nihaoa 1wo 34shi shei ne'))

print(re.findall('[\W ]', '_nihaoa 1wo 34shi shei ne'))
print(re.findall('[\s]', 'nihaoa 1wo 34shi she\nsddse'))

#  re.M is used to all lines
# ^ is head    but \A is used to only the head  although many lines

print('########################')

print(re.search('^nihaoa', 'nihaoa 1wo shi shei ne'))
print(re.search('\Anihaoa', 'nihaoa 1wo shi shei ne'))

print(re.findall('^nihaoa', 'nihaoa 1wo shi \nnihaoa  shei ne', re.M))
print(re.findall('\Anihaoa', 'nihaoa 1wo shi \nnihaoa  shei ne', re.M))

print(re.findall('shi$', 'nihaoa 1wo shi\n nihaoa  shei ne shi', re.M))
print(re.findall('shi\Z', 'nihaoa 1wo shi\n nihaoa  shei ne shi', re.M))

#the bonudry of a word      \b need a r""
print(re.search(r'er\b', 'never'))
print(re.search(r'er\b', 'nerve'))
print(re.search('er\B', 'never'))
print(re.search('er\B', 'nerve'))


print('###################################')



print(re.findall(r'a?', 'aaaDaaaaaaaDaaaa'))
print(re.findall(r'a+', 'aaaDaaaaaaaDaaaa'))
print(re.findall(r'a*', 'aaaDaaaaaaaDaaaa'))

print(re.findall(r'a{3}', 'aaaDaaaaaaSaaaa'))
print(re.findall(r'a{3,}', 'aaaSaaaaaaaDaaaa'))
print(re.findall(r'a{3,4}', 'aaaDaaaaaaaSaaaa'))
print(re.findall(r'((s|S)unck)', 'Sunck---sunck'))


#  *?  +?   x?    min matching


print(re.findall(r'i.*man', 'i am a good man i am a good man i am a good man'))
print(re.findall(r'^i.*man$', 'i am a good man i am a good man i am a good man'))

print(re.findall(r'i.*?man', 'i am a good man i am a good man i am a good man'))


'''
6666-1234567890 qq
mail suncksunck@163.com
phone  010-5536789
'''

# print(re.match(r'\d{4,10}', '1234567890'))
#print(re.match(r'\D{1,}@(163|126).(com|cn)' ,'suncksunck@163.com'))

s = '362321567891051234'
res1 = re.search('(?P<shishei>\d{4})', s)
print(res1.groupdict())

str = '15345678901'
data = re.findall(r'\b1[3456789][0-9]\d{8}', str)

print(data)
