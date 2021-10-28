# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python
File Name：     demo9_for
Description :   迭代和循环
                迭代可以看作是循环的高效版本
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 17:38
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
# 集合迭代
a = [1, 2, 3, 4, 5]


def my_fun(x):
    print('do something on ', x)
    return x + 1


# 迭代版本
b = [my_fun(x) for x in a]
print(b)  # 输出：[2, 3, 4, 5, 6]

# 循环版本
b2 = []
for x in a:
    t = x + 1
    b2.append(t)
print(b2)  # 输出：[2, 3, 4, 5, 6]

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