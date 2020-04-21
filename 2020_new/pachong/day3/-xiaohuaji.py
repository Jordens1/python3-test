#/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.request, urllib.parse
import re, gzip
from bs4 import BeautifulSoup

'''
爬取指定页面的标题和内容，保存到html文件中，标题用h1，内容用p。不要图片，追加，
'''
#http://www.jokeji.cn/list5_3.htm
#https://www.zhuici.com/rank_www.yikexun.cn-2.html

url = r"http://www.jokeji.cn/"

header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }

start_ye = input("请输入开始页")
end_ye = input("请输入结束页")
for i in range(int(start_ye), int(end_ye)+1):
    url = url + "list5_" + str(i) + ".htm"
    # print(url)
    request = urllib.request.Request(url, headers=header)
    reponse = urllib.request.urlopen(request)
    reponse = reponse.read().decode("gb2312", "ignore")
    pattern = re.compile(r'<li><b><a href="(.*?)"target="_blank" >(.*?)</a></b><span>.*?</li>')
    ret = pattern.findall(reponse)
    # print(len(ret))
    for i in range(len(ret)):
        title = ret[i][-1]
        neiurl = r"http://www.jokeji.cn" + ret[i][0]
        reponse1 = urllib.request.Request(neiurl, headers=header)
        request1 = urllib.request.urlopen(reponse1)
        pattern1 = re.compile(r'<span id="text110"><P>(.*)</P></span>', re.S)
        ret1 = pattern1.findall(request1.read().decode("gb2312", "ignore"))
        # neirong = request1.read().decode("gb2312", "ignore")
        #替换掉图片
        # pattern3 = re.compile(r'>*.jpg')
        # ret3 = pattern3.sub("", ret1)
        with open(title + ".txt", "w", encoding="gb2312") as f:
            f.write(ret1[0])















