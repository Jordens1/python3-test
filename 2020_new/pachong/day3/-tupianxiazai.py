#/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib.request, urllib.parse, re
#图片爬取，按页数爬取，存到文件夹里，
url = r"https://www.litailun.com/Qiche/index/p/"
header = {"User-Agent": "User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", }

start_ye = input("请输入开始页")
end_ye = input("请输入结束页")

# print(reponse)
for i in range(int(start_ye), int(end_ye) + 1):
    rel_url = url + str(i) + ".html"
    request = urllib.request.Request(rel_url, headers=header)
    reponse = urllib.request.urlopen(request).read().decode()
    ret = re.compile(r'<li style="width:23%;height:180px;"><a target="_blank" href="/qiche/\d+.html" title="(.*?)">\n<img src="(.*?)" alt="(\1)">', re.S)
    pattern = ret.findall(reponse)
    for j in range(len(pattern)):
        turl = "http:" + pattern[j][1]
        request1 = urllib.request.Request(turl, headers=header)
        reponse1 = urllib.request.urlopen(request1)
        with open(pattern[j][0] + ".JPG", "wb") as f:
            f.write(reponse1.read())
