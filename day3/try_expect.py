import sys,time,os
import traceback

#注意进去之后的指针问题,课件上的例题
with open('b.txt', 'r') as f :
    content_list = f.read().split('\n')
    #print(content_list)
lines = []

for line in content_list:
    # print(line, type(line))
    if 'click_sum' in line:
        _, click_sum, percent = line.split()
        sum = click_sum.split(':')[-1]
        per = percent.replace('%', '').split(':')[-1]

        try :
            sum = int(sum)
            per = float(per)
            if sum > 100 and per > 30 :
                lines.append([per, line])
                # print(lines)
        except Exception as e :
            print("获取到的数据不是数字类型的，无法装换比较")
            print(traceback.format_exc())
            # print()
#print(lines)

lines.sort(key=lambda item :item[0], reverse=True)

#print(lines)

for line in lines :
    print(line[-1])

