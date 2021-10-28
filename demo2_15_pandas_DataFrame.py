# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo2_15
Description :   Pandas 基础
                DataFrame 是数据分析中使用最多的数据结构，其大部分数据也是以表格形式存储的。
                (Python 的 Pandas 库有 DataFrame，R 语言中也有类似 DataFrame 的数据结构。)
                在数据库领域中表的概念就是一个 DataFrame，因此学好 DataFrame 是数据分析的基础。
                DataFrame 其实就是一张表，如一张 Excel 表就是一个 DataFrame。

                Table:
                索引  |   学号  |   姓名  |   身高  |   语文成绩    |   学分  |   日期
                        string  string      int         int       float    日期型

Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020/11/29 下午11:09
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020/11/29:
-------------------------------------------------
"""
# DataFrame 表格数据 1
import pandas as pd

df1 = pd.DataFrame(data={
    '学号': ['x1', 'x2', 'x3', 'x4', 'x5'],
    '姓名': ['张三', '李四', '王五', '韩六', '赵七'],
    '身高': [177, 151, 167, 175, 153],
    '语文成绩': [92, 84, 80, 77, 87],
    '学分': [1.5, 2.3, 3.2, 1.2, 1.8],
    '日期': ['2019/3/23', '2019/3/24', '2019/3/25', '2019/3/26', '2019/3/27']
})

print('\n表格1：\n')
print(df1)   # 输出有问题，从姓名列开始不对齐，需要找一下 Reason

# DataFrame 表格数据 2

df2 = pd.DataFrame(data=[
    ['x1', '张三', 177, 92, 1.5, '2019/3/23'],
    ['x2', '李四', 151, 84, 2.3, '2019/3/24'],
    ['x3', '王五', 167, 80, 3.2, '2019/3/25'],
    ['x4', '韩六', 175, 77, 1.2, '2019/3/26'],
    ['x5', '赵七', 153, 87, 1.8, '2019/3/27'],
],
    columns=['学号', '姓名', '身高', '语文成绩', '学分', '日期']
)

print('\n表格2：\n')
print(df2)
