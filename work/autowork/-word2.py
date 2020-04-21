#/usr/bin/env python
# _*_ coding:utf-8 _*_

#读取并写入其他的文件中
import win32com
import win32com.client

def writeWrod(path, topath):
    mw = win32com.client.Dispatch('Word.Application')
    doc = mw.Documents.Open(path)

    #将内容保存到另一个文件中
    doc.SaveAs(topath, 2)   #2表示为txt文件


    doc.Close()
    mw.Quit()

# path = r'C:\python3test\视在\autowork\实验.docx'
# topath = r'C:\python3test\视在\autowork\写入.txt'
# writeWrod(path, topath)

import os

def createWord(path):
    word = win32com.client.Dispatch('Word.Application')
    #让文档可见
    word.Visible = True
    #创建文档
    doc = word.Documents.Add()
    #写内容，从头开始写
    r = doc.Range(0, 0)
    r.InsertAfter('我看见雨滴落在青青草地')
    r.InsertAfter('小艾同学')
    # 存储文件
    doc.SaveAs(path)
    # 关闭文件
    doc.Close()
    #退出word
    word.Quit()

name = ['章' ,'李', '王']
for i in name:
    path = os.path.join(os.getcwd(), i)
    createWord(path)





