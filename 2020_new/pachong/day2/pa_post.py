#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
x-requested-with: XMLHttpRequest  有这个就是rdx请求方式
post 方式： urllib.request.urlopen(url, data= )


'''
import urllib.request, urllib.parse

url = "https://fanyi.baidu.com/sug"
word = input("输入")
form_data = {"kw": word}
#处理表单数据
form_data = urllib.parse.urlencode(form_data)
headers = {"User-Agents": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
#构建请求对象
requesta = urllib.request.Request(headers= headers, url= url)
#发送请求
reponse = urllib.request.urlopen(url, data= form_data.encode())

print(reponse.read().decode())






