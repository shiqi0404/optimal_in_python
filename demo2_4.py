# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo2_4
Description :   Python 字典
                字典是除列表外使用最广泛的数据结构，常用来存储数据映射。
                字典由 key (键) 和 value (值) 组成，其中 key 在一个字典中是不会重复的。
                例：一本书来说，书目录 是一个字典，章节标题 是 key，页码 是 value。
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 16:30
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
# Python 字典：dict
da = {'a': 123, 'b': 456, 'c': 789}     # 创建一个简单的字典，由3个映射构成
db = {'a': [1, 2, 3], 'b': [4, 5, 6]}   # 一个复杂的字典，值是 list(列表) 结构

print('字典da的映射数量是: ', len(da))                # 输出：3
print('字典da，key=b 的映射值是: ', da.get('b'))      # 输出：456
print('键d 是否存在在字典da的键集合中: ', 'd' in da)  # 输出：False

# 查看所有映射关系
for key, value in da.items():
    print(key, '=', value)
# a = 123
# b = 456
# c = 789

# 添加或删除映射关系
da['d'] = 10    # 添加 'd'
da.pop('a')     # 删除 'a'
print(da)       # {'b': 456, 'c': 789, 'd': 10}
