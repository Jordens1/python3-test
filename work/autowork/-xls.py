#/usr/bin/env python
# _*_ coding:utf-8 _*_

#有序字典
from collections import OrderedDict
#读取数据
from pyexcel_xls import get_data

#读取xls或者是slsx数据
def readXls(path):
    dic = OrderedDict()
    #抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

path = r'C:\python3test\视在\autowork\b.xlsx'
c = readXls(path)
print(c)

#写入数据  可以xlsx 换一个数据格式
from pyexcel_xls import save_data
def writeXls(path, date):
    dic = OrderedDict()
    for sheetName, sheetValue in date.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)
    save_data(path, dic)

path = r'C:\python3test\视在\autowork\a.xls'
date = {'表1': [[1, 2, 3], [4, 5, 6], [7, 8, 9]], '表2': [[11, 22, 33], [44, 55, 66], [77, 88, 99]]}
writeXls(path, date)







