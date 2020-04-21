#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
urlERROR:没网、连接服务器失败、找不到服务器
httpERROR：是 urlERROR的子类，
import urllib.error

'''
import urllib.request, urllib.parse
import urllib.error

url = "https://www.cnblogs.com/xieshengsen/p/687651.html"

try:

    reponse = urllib.request.urlopen(url)

    print(reponse)
except Exception as e:
    print(e)

except urllib.error.HTTPError as e:
    print(e)
    print(e.code)

except urllib.error.URLError as e:
    print(e, e.code)



