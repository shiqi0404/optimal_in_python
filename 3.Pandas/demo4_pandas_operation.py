# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo4_pandas_operation
Description :   
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 13:07
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""
# DataFrame 表格数据
import pandas as pd

df = pd.DataFrame(data={
    '学号': ['x1', 'x2', 'x3', 'x4', 'x5'],
    '姓名': ['张三', '李四', '王五', '韩六', '赵七'],
    '身高': [177, 151, 167, 175, 153],
    '语文成绩': [92, 84, 80, 77, 87],
    '学分': [1.5, 2.3, 3.2, 1.2, 1.8],
    '日期': ['2019/3/23', '2019/3/24', '2019/3/25', '2019/3/26', '2019/3/27']
})
