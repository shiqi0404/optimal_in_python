# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo2_5
Description :   Python 集合
                是一个无序的不重复元素序列，集合操作包含 交集、并集、差集等。
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 16:41
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
# Python 集合：set
sa = {'a', 'b', 'c', 'd'}
sb = {'b', 'c', 'f'}

print('sa集合为: ', sa)
print('sb集合为: ', sb)
print('元素a 是否在集合sa中: ', 'a' in sa)  # 输出：True

print('交集: ', sa & sb)  # 输出：{'b', 'c'}
print('并集: ', sa | sb)  # 输出：{'a', 'b', 'c', 'd', 'f'}
print('差集: 在sa中而不在sb中的元素: ', sa - sb)   # 输出：{'a', 'd'}
print('不同时包含在sa和sb中的元素: ', sa ^ sb)     # 输出：{'d', 'a', 'f'}
