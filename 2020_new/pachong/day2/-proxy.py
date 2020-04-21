#/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.request, urllib.parse

#创建handler
handler = urllib.request.ProxyHandler({"http": "47.100.35.138:22"})
#创建opner
opener = urllib.request.build_opener(handler)

url = "https://cn.bing.com/search?q=ip&PC=U316&FORM=CHROMN"

header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }

request = urllib.request.Request(url, headers=header)

reponse = opener.open(request)

with open("proxy.html", "wb") as f:
    f.write(reponse.read())





