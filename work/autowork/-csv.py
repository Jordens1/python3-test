#/usr/bin/env python
# _*_ coding:utf-8 _*_
import csv

#读csv文件
def readCsv(path):
    Infolist = []
    with open(path, 'r') as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            Infolist.append(row)
    return Infolist
# path = r'C:\python3test\视在\autowork\a.csv'
# readcsv = readCsv(path)


def writeCsv(path, date):
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for rowdate in date:
            writer.writerow(rowdate)

date = (['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'])
path = r'C:\python3test\视在\autowork\b.csv'







