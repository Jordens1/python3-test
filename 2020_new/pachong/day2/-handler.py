#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
urlopen()  发送请求，获取响应
Request（）  定制请求头，创建请求对象

高级功能：使用代理，cookies
Handler   Opener

代理：浏览器配置、

'''
import urllib.request, urllib.parse

url = "http://www.baidu.com/"
header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }

#创建一个handler
handler = urllib.request.HTTPHandler()
#通过handler创建一个opner, opner就是一个对象发送请求就是直接使用opner方法
opener = urllib.request.build_opener(handler)
#构建请求对象
request = urllib.request.Request(url, headers=header)
#发送请求
reponse = opener.open(request)
print(reponse.read().decode())



