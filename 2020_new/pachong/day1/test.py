#/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib.request, urllib.parse

imput_name = input("输入名字")
url1 = "http://www.baidu.com/s?"
date = {"wd": imput_name, "rsv_spt": 1}
query_url = url1 + urllib.parse.urlencode(date)

#urllib.request.urlopen(query_url)
urllib.request.urlretrieve(query_url, imput_name + ".html")


