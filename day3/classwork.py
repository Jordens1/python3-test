import sys,time,random,os,copy


#由用户输入4个不同数字，程序输出由这些数字组成的不同顺序的4位数

in_str = input("please input four different nums : ")
in_list = list(in_str)
in_list2 = list(set(in_str))
int1 = in_list
sum1 = 0

if len(in_list) != len(in_list2) or len(in_list2) != 4 :
    print("wrong nums, input again")
else :
    for i in int1:
        for n in int1:
            for j in int1:
                for k in int1:
                    if i != j and i != n and i != k and j !=n and j!= k and n != k:
                        print(i+n+j+k)
                        sum1 +=1
print(sum1, 'ge')






