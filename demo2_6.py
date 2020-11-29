# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo2_6
Description :   Python 函数定义和调用
                定义找最大值的函数，然后再定义
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 16:57
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
# Python 函数定义和调用
def find_max(a, b, c):
    """
    定义一个函数 find_max, 实现的功能是找到 a、b、c中的最大值
    该函数需要输入3个参数，分别是a、b、c，返回值是3个参数的最大值
    """
    max_number = None
    if a > b and a > c:
        max_number = a
    elif b > a and b > c:
        max_number = b
    elif c > a and c > b:
        max_number = c
    return max_number

# 使用刚才定义的函数
max_num = find_max(a=1, b=2, c=3)
print('最大的数是: ', max_num)           # 输出：3

# Python 内部已经实现了该函数，直接调用即可
print('最大的数是: ', max([1, 2, 3]))    # 输出：3
