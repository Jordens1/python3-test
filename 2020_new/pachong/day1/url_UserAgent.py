#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
伪装UA， 让服务端认为是浏览器在上网， urllib.request.Request()



'''
import urllib.request, urllib.parse

url1 = "http://www.baidu.com/"
#伪装头部
header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }
#请求对象
request = urllib.request.Request(url=url1, headers=header)
#发送
reponse = urllib.request.urlopen(request)
print(reponse.read().decode())