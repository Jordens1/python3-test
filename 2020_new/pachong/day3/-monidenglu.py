#/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.request, urllib.parse


#登录完进行cookie的保存， 使用cookiejar
import http.cookiejar
cj = http.cookiejar.CookieJar()
#通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
#根据handler创建一个opener, 后面发送请求都使用opener
opener = urllib.request.build_opener(handler)


#post模拟登录
post_url = "https://mail.163.com/contacts/call.do?uid=m18270938391@163.com&sid=aBlipYEbVzLMielMKwbbeUYlARbthYWy&from=webmail&cmd=newapi.getContacts&vcardver=3.0&ctype=all&attachinfos=yellowpage,frequentContacts&freContLim=20"
header = ""
request = urllib.request.Request(post_url, headers=header)
date = {}
date = urllib.parse.urlencode(date).encode()
reponse = opener.open(request, data=date)


#已经登录，进行get验证
get_url = ""
request2 = urllib.request.Request(url, headers=header)
#省略
reponse2 = opener.open(request2)
















