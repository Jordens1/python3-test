import copy

list1_1 = [0, 1, 2, ['a', 'b']]
list1_2 = list1_1                   # 赋值
list1_3 = list1_1.copy()            # 浅拷贝;同 list1_3 = list1_1[:]
list1_4 = copy.copy(list1_1)        # 浅拷贝
list1_5 = copy.deepcopy(list1_1)    # 深拷贝

# 打印出拷贝后的 list1_1 ~ list1_5
print("list1_1 =", list1_1)
print("list1_2 =", list1_2)
print("list1_3 =", list1_3)
print("list1_4 =", list1_4)
print("list1_5 =", list1_5)
print('-'*40)                       # 分割线

list1_1.append(4)                   # 在 list1_1 末尾添加一个元素 4
list1_1[3].append('c')              # 向 list1_1 中内嵌的列表末尾添加一个元素 'c'

# 打印出更改后的 list1_1 ~ list1_5
print("list1_1' =", list1_1)
print("list1_2' =", list1_2)
print("list1_3' =", list1_3)
print("list1_4' =", list1_4)
print("list1_5' =", list1_5)