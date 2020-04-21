#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
. 任意一个
[]  里面的任意一个
\d 数字
\s 空白字符
\w 数字、字母、下划线、中文

{3} 匹配前面字符3次

（） 整体 分组  \1  \2

.* 无法匹配换行符   需要re.S

? 非贪婪匹配

re.I   忽略大小些
re.M   多行匹配
re.S    单行匹配

re.sub(正则， 替换内容， 字符串)   或者   a = re.compile     a.sub(替换内容， 字符串)
'''
import re

string = "<p><div><span>猪八戒</sapn></div></p>"
pattern = re.compile(r"<(/\w+)><(/\w+)><(/\w+)>", re.I)
ret = pattern.search(string)
print(ret.group())


string1 = "<>aaa\n, abbbb\n, accc<>"
pattern = re.compile(r"<>(.*)<>")
ret = pattern.findall(string1, re.S)
print(ret)



#将里面的匹配到的东西进行处理然后返回替换
def fn(a):
    # print(type(a))
    c = int(a.group())
    return str(c - 10)

string3 = r"我喜欢身高189"

pattern2 = re.compile(r"\d+", re.S)
ret = pattern2.sub(fn, string3)
print(ret)




