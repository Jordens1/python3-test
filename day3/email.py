import sys,time,random,os,copy

#由用户输入4个不同数字，程序输出由这些数字组成的不同顺序的4位数

in_str = input("please input four different nums : ")
in_list = list(in_str)
in_list2 = list(set(in_str))

if len(in_list) != len(in_list2) or len(in_list2) != 4 :
    print("wrong nums, input again")
else :
    for i in range(4):
        in_list_1 = copy.deepcopy(in_list)

        mov_num = in_list_1.pop(i)

        for n in range(3):
            in_list_2 = copy.deepcopy(in_list_1)

            in_list_2.insert(n, mov_num)

            print(in_list_2)

            






