#/usr/bin/env python
# _*_ coding:utf-8 _*_

import xlwings as xw


import xlwings as xw
app=xw.App(visible=True,add_book=False)
#新建一个表格
# wb=app.books.open(r"C:\Users\Darnell\Desktop\test.xlsx")
# wb.save()

#打开一个已经存在的表格
wb=app.books.add()
# wb.save(r"C:\Users\Darnell\Desktop\test-1.xlsx")
wb.activate()       #  激活为当前工作簿,可能存在多个表在工作
#在单元格输入数据  sheet要存在
wb.sheets["sheet1"].range("A2").value="xishi"
rng=xw.Range('A1')
# 加入超链接
rng=xw.Range('A1')
rng.add_hyperlink(r'www.baidu.com','百度',"提示：点击即链接到百度")
# 设置range的颜色
rng.color=(255,255,255)
# 获得列宽
a = rng.column_width
print(a)
#返回range的总宽度
b = rng.width
print(b)
# range的总行数
rng.rows.count
# 返回range的所有列
rng.columns
# 返回range的第一列
rng.columns[0]
# 返回range的列数
rng.columns.count

# 将a1,a2,a3输入第一列，b1,b2,b3输入第二列
list1=[["a1",'a2','a3'],['b1','b2','b3']]
xw.range('A1').value=list1

# 选取第一列
sht=xw.sheets.active
rng=sht.range('A1').expand('down')
rng.value=['a1','a2','a3']

# 选取第一行
rng=sht.range('A1').expand('right')
rng=['a1','b1']

# 选取表格
rng.sht.range('A1').expand('table')
rng.value=[["a1",'a2','a3'],['b1','b2','b3']]


wb.save(r"C:\Users\Darnell\Desktop\test-1.xlsx")
wb.close()
app.quit()


