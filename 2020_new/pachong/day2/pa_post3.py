#/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.request, urllib.parse

#xhr 的例子，就是json格式   豆瓣

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

start  = int(input("输入start"))
date = {"start" :start, "limit": 3}
header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }
start = urllib.parse.urlencode(date)

rel_url = url + start
requse = urllib.request.Request(url=rel_url, headers=header)
reponse = urllib.request.urlopen(requse)
print(reponse.read().decode())

# KFC  post方式
import urllib.request, urllib.parse
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

date = {"cname": "安庆",
        "pid": "" ,
        "pageIndex": "1",
        "pageSize": "10"}

header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }

date = urllib.parse.urlencode(date).encode()
repuest = urllib.request.Request(url=url, headers=header)

reponse = urllib.request.urlopen(repuest, data=date)
print(reponse.read().decode())









