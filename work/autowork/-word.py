#/usr/bin/env python
# _*_ coding:utf-8 _*_

#读取doc和docx   最稳定的库
import win32com
import win32com.client

def readWord(path):
    #调用系统的word功能，可以处理doc和docx文件格式
    mw = win32com.client.Dispatch('Word.Application')
    #打开文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出
    mw.Quit()

path = r'C:\python3test\视在\autowork\实验.docx'
readWord(path)







