#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
根据url爬取a链    sublime编辑器（强大）
scrapy框架 强大
抓取网页  采集数据  数据处理  提供检索服务
给url  访问url  解析内容，提取数据

使用的库:urllib\requests\bs4
解析时的知识：正则表达式、bs4、xpath、jsonpath

fiddler  抓包工具:网页右键-network、fiddler

urllib库：
python2：urllib urllib2

python3：urllib.request  urllib.parse

urllib.request :urlopen  urlretrieve
reponse ： read()  geturl()  getheaders() getcode() readlines()
urllib.parse : quote   unquote   urlencode


'''
import urllib.request


url = "https://www.baidu.com/"

reponse = urllib.request.urlopen(url)

#read 方法    encode（）字符串——》二进制，默认utf-8/gdk(看网页编码)  decode（）  相反
# with open('baidu.html', 'w', encoding='utf-8',) as f:
#     f.write(reponse.read().decode())

print(reponse.geturl())
#获取头部信息，可以转换成字典取值
print(dict(reponse.getheaders()))
#获取状态码
print(reponse.getcode())
#按行读取，返回列表，都是字节类型
print(reponse.readlines())

#下载图片  二进制格式
image_url = "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&step_word=&hs=2&pn=19&spn=0&di=65670&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3622049944%2C285954675&os=3899481471%2C2098302306&simid=3564992377%2C464958107&adpicid=0&lpn=0&ln=1960&fr=&fmq=1582974585074_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=girl&bdtype=0&oriquery=&objurl=http%3A%2F%2F01.minipic.eastday.com%2F20161210%2F20161210104540_a0e8cd44f13a9547544dd50f1a61c694_1.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3F4tgtt42_z%26e3Bjwfp1wy_z%26e3Bv54AzdH3F1jpwtsAzdH3F8m8d8a8a9c9amnmcm8nd0_z%26e3Bip4s&gsm=16&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
#reponse2 = urllib.request.urlopen(image_url)
# with open('image.jpg', 'wb+') as f:
#     f.write(reponse2.read())  等价于下面的方法
urllib.request.urlretrieve(image_url, "./test.jpg")




