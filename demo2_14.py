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