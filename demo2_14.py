# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo2_14
Description :   Pandas 基础
                Numpy 是科学计算的核心，Pandas 是 Python 数据分析事实上的标准；
                Pandas 的核心也是 Numpy，Pandas 是在 Numpy 的基础上封装了高级接口。
                Pandas 提供了 Series 和 DataFrame 两种基础数据结构，
                Series 表示序列数据；DataFrame 表示表格数据，且是由多个 Series 组成的。
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
s = pd.Series(data=value, index=index)
print(s)
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
