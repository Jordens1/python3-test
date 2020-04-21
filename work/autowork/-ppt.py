#/usr/bin/env python
# _*_ coding:utf-8 _*_
import win32com
import win32com.client

def writePpt():
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    #增加一个文件
    pptFile = ppt.Presentations.Add()
    #创建页  参数一：页数    参数二：类型
    page1 = pptFile.Slides.Add(1, 1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "xishi"
    t2 = page1.Shapes[0].TextFrame.TextRange
    t2.Text = "diaocan"

    page2 = pptFile.Slides.Add(2, 1)
    t2 = page2.Shapes[0].TextFrame.TextRange
    t2.Text = "diaocan"

    page3 = pptFile.Slides.Add(3, 2)
    t3 = page3.Shapes[0].TextFrame.TextRange
    t3.Text = "guifei"
    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()



path = r'C:\python3test\视在\autowork\a.xls'
writePpt(path)















