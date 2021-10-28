# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo1_pandas_Series
Description :   Pandas 基础

                Numpy 是科学计算的核心，Pandas 是 Python 数据分析事实上的标准；
                Pandas 的核心也是 Numpy，Pandas 是在 Numpy 的基础上封装了高级接口。

                Pandas 提供了 Series 和 DataFrame 两种基础数据结构，
                Series 表示序列数据；DataFrame 表示表格数据，且是由多个 Series 组成的。

                Series 可以看成是字典结构，包括 索引 (字典中的 key(键)) 和 值 (字典的 value(值))
                Series 底层数据结构使用 Numpy 存储，不仅能使存储计算效率更高，还针对数据分析领域封装了很多实用的函数接口。

                Table:
                索引(日期)  |   值(气温)

Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020/11/29 下午9:59
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020/11/29:
-------------------------------------------------
"""
# Series 序列数据
import pandas as pd

# Series 的索引
index = ['2019/3/23', '2019/3/24', '2019/3/25', '2019/3/26', '2019/3/27',
         '2019/3/28', '2019/3/29', '2019/3/30', '2019/3/31', '2019/4/1',
         '2019/4/2', '2019/4/3', '2019/4/4']

# Series 的值
value = [18, 20, 19, 20, 18, 15, 17, 19, 20, 15, 18, 15, 20]

# 创建 Series
# 如果不指定索引，会自动生成 0，1，2，...这样的索引
s0 = pd.Series(data=value)
print('默认索引:\n', s0)
# 默认索引:
# 0     18
# 1     20
# 2     19
# 3     20
# 4     18
# 5     15
# 6     17
# 7     19
# 8     20
# 9     15
# 10    18
# 11    15
# 12    20
# dtype: int64
s = pd.Series(data=value, index=index)
print('指定索引:\n', s)
# 指定索引:
# 2019/3/23    18
# 2019/3/24    20
# 2019/3/25    19
# 2019/3/26    20
# 2019/3/27    18
# 2019/3/28    15
# 2019/3/29    17
# 2019/3/30    19
# 2019/3/31    20
# 2019/4/1     15
# 2019/4/2     18
# 2019/4/3     15
# 2019/4/4     20
# dtype: int64
