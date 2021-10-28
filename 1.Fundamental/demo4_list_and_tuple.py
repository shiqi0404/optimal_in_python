# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python
File Name：     demo4_list and tuple
Description :   Python 列表 元组
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 15:59
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
# Python 列表: list
la = [1, 2, 3, 4]   # 创建一个列表，包含4个元素
lb = ['a', 'b', 'c']    # 创建一个列表，包含3个元素

print('列表la的元素个数是: ', len(la))  # 输出：4
print('取出第1个元素: ', la[0])         # 输出：1  Python中序号是从0开始
print('取出最后一个元素: ', la[-1])     # 输出：4
print('取出从第0到第2个元素: ', la[0:3])    # 输出：1 2 3  [0:3]表示从第0到第2(3-1=2)个元素 => 数学的右开区间 [0,3)
print('取出从第0到第2个元素: ', la[:3])    # la[:3] = la[0:3]，同理，la[3:] 表示从第3个元素开始到最后一个
print('取出从第3到最后元素: ', la[3:])      # 输出：4     la[3:] 表示从第3个元素开始到最后一个

# 修改第2个元素
la[1] = 5
print(la)   # 输出：[1, 5, 3, 4]

# 列表删减元素
la.append(5)    # 在列表末尾添加一个元素 5 => la = [1, 5, 3, 4, 5]
la.pop(2)       # 删除第3个元素            => la = [1, 5, 4, 5]
print(la)       # 输出：[1. 5. 4. 5]

# 列表迭代，相当于for循环
for index, value in enumerate(la):
    print('第 %d 个元素的值是: %d' % (index, value))
# 第 0 个元素的值是 1
# 第 1 个元素的值是 5
# 第 2 个元素的值是 4
# 第 3 个元素的值是 5

# 使用二维列表来模拟矩阵，二维列表就是列表中嵌套列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print('取出矩阵的第2行第2个元素是: ', matrix[1][1])     # 输出：5

# Python 元组: tuple
# 元组与列表区别在于 1.元组的元素不能被修改；
#                    2.列表用 []，元组用 ()
ta = ('a', 'b', 'c')    # 创建一个元组，包含3个元素

print('元组ta的元素个数是: ', len(ta))  # 输出：3
print('取出第1个元素是: ', ta[0])       # 输出：a
print('取出最后一个元素是: ', ta[-1])   # 输出：c

# 元组迭代
for v in ta:
    print(v)    # 依次输出 a b c

