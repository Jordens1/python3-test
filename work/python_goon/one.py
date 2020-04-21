#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
找到 click_sum 的值大于 100 且 percent 的值大于 30% 的数据，并且
按照 percent 的值 进行由大到小进行排序打印出来

'''

with open(r"C:/python3test/视在/shuju-test.txt", "r") as f:
    content_list = f.readlines()
    list = []
    for line in content_list:
        #print(line)
        if "percent" in line:
            sum = line.split(" ")[1].split(":")[1]
            perc = line.split(" ")[2].split(":")[1].replace("%", "")
            #print(sum,  perc)
            if float(sum) > 100 and float(perc) > 30:
                list.append([float(sum), line])
                list.sort(key=lambda item: item[0], reverse=True)
                for i in list:
                    print(i[1], end="")

















