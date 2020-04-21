#/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib.request, urllib.parse

url = "https://tieba.baidu.com/f?"
a = int(input("起始页数： "))

pn = int(input("最后的页数： "))  #输入页数
kw = input("贴吧的名字： ")  # 输入贴吧名
j=0
while j < 3:
    j += 1
    for i in range(a, pn + 1):
        date = {"kw": kw, "ie": "utf-8", "pn": (i-1)*50}
        header = {
            "User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }
        date = urllib.parse.urlencode(date)
        url += date

        request = urllib.request.Request(url=url, headers=header)

        reponse = urllib.request.urlopen(request)
        with open(kw + str(i) + ".html", "wb") as f:
            f.write(reponse.read())









