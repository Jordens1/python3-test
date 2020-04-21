#/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.parse

#url只能由特定的字符组成，字母、下划线，其他的需要编码  就像后面的%f
image_url1 = "https://cn.bing.com/images/search?view=detailV2&ccid=%2bGt%2fVxUz&id=41C720EB8B7E7FD574AA7138A18D6455F3EEDDFE&thid=OIP.-Gt_VxUzNaMT5C9Mt1FdLwHaKN&mediaurl=http%3a%2f%2fpic1.sc.chinaz.com%2fFiles%2fpic%2fpic7%2fpic5329.jpg&exph=842&expw=611&q=%e7%be%8e%e5%a5%b3%e5%9b%be%e7%89%87&simid=608032768644678409&selectedIndex=1&ajaxhist=0"
#汉字编码
image_url = "www.baidu.com/images?name=狗蛋"
url_hanzi = urllib.parse.quote(image_url)
print(url_hanzi)
#汉字反编码
url_fanhanzi = urllib.parse.unquote(url_hanzi)
print(url_fanhanzi)

# 假如url参数有 name age sex height
name = "xishi"
age = 18
sex = "男"
height = "180"
#如何放进去
date = {"name": name, "age": age, "sex": sex, "height":height}
l = []
for k, v in date.items():
    l.append(k + "=" + str(v))
query_str = "&".join(l)
#以上的可以用下面的代替，有汉字也可以转换编码
query_str = urllib.parse.urlencode(date)
image_url = image_url + "?" + query_str
print(image_url)
























