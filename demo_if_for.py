# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo_if_for
Description :   程序控制语句： 条件判断、 循环控制
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 16:51
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
#  条件判断
a = [1, 2, 3]
if 1 in a:
    print('元素1包含在列表a中')
else:
    print('元素1不包含在列表a中')

# 循环控制
# 1. 对某个数据集合进行迭代，满足条件时跳出循环
b = [1, 2, 3, 4]
for i in b:
    if i > 3:
        break   # 满足条件时跳出循环
    print(i)

# 2. 通过循环知道满足条件
c = 1
while c < 10:
    c = c + 1
    print('%d do something also.' % (c - 1))
print(c)

