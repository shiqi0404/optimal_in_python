# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo2_8
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
