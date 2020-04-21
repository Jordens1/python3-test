#/usr/bin/env python
# _*_ coding:utf-8 _*_

import hashlib

'''
加密算法的都在里面
md5   sha1 sha256 单向的
base64  可逆的     有网址在线加密解密
'''
#传递的是编码的
msg = '中午一起吃饭'
mimi = hashlib.md5(msg.encode('utf-8'))
# 显示16进制看
print(mimi.hexdigest())


sha1 = hashlib.sha1(msg.encode('utf-8'))
# 显示16进制看
print(sha1.hexdigest())


sha = hashlib.sha256(msg.encode('utf-8'))
# 显示16进制看
mimi = sha.hexdigest()
print(mimi)


#密码验证
mima = [mimi]
yanzheng = input("输入密码")
yanzheng = hashlib.sha256(yanzheng.encode('utf-8'))
yanzheng = yanzheng.hexdigest()
for i in mima:
    if i == yanzheng:
        print("ok")


#更新   计算hash值
def main():
    #生成hash摘要器
    digster = hashlib.md5()
    with open('', 'rb') as f:
        # data = f.read(1024)
        # while data:
        #     digster.update(data)
        #     data = f.read(1024)
        #上面的等价为下面的迭代器
        diedia = iter(lambda :f.read(1024), b'')
        for data in diedia:
            digster.update(data)
    print(digster.hexdigest())
