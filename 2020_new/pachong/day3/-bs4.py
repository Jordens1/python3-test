#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
换源方式
%appdata%   新建pip文件  pip.ini文件
vim ~/.pip/pip.conf

lxml, bs4两个模块
说明：选择器， jquery
'''

#可以将html文档转换成指定的对象，然后查找指定的内容
from bs4 import BeautifulSoup

#转换本地文件
soup = BeautifulSoup(open('test.html', encoding='utf-8'), "lxml")

#一个对象
#print(soup, type(soup))

#按照标签名字查找
print(soup.a, type(soup.a))

# 获取所有的属性和值   获取href,name属性
print(soup.a.attrs)
print(soup.a["href"], soup.a["name"])
print(soup.a.attrs["name"],"#"*10)

#获取内容，如果标签里还有标签，则string获取的为none，其他连个可以获取内容
print(soup.a.string,"#"*10)
print(soup.text,"#"*10)
print(soup.get_text(),"#"*10)

#find方法  还可以一层一层的套用find
print(soup.find("a"))  #找第一个a,也可以增加限制条件 title="2"

#find_all 可以加条件，和限制
div = soup.find('div', class_="tang")
print(div.find_all("a"))
print(div.find_all("a", limit=1))
print(div.find_all(["a", "b"]))
print("#"*10)
'''
select 根据选择器去选择指定的内容
标签选择器、类选择器、id选择器、并集、层级、伪类、属性选择器
div .dudu #lal .meme   下面好多级
div > p   下面一级

select返回的永远是列表，也可以是多层调用
'''
print(soup.select(".tang > ul > li > a")[1])
print(soup.select("cc"))

'''
下面自己测试一下
'''

# url = r'https://www.litailun.com/Qiche/index/p/3.html'
# header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }
#
# request = urllib.request.Request(url, headers=header)
# reponse = urllib.request.urlopen(request).read().decode()
# with open('bs4.html', 'w', encoding='utf-8') as f:
#     f.write(reponse)

#soup = BeautifulSoup(open('bs4.html', encoding='utf-8'), 'lxml')
# print(soup.div)
# print(soup.div['class'])
# a = soup.find('div', class_='had3_2')
# b = a.find_all('li')