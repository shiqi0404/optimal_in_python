# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo5_pandas_groupby
Description :   分组统计 应用 groupby 函数进行分组统计
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 17:59
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""

import pandas as pd

data = {
    '学号': ['x1', 'x2', 'x3', 'x4', 'x5'],
    '班级': ['1班', '2班', '3班', '4班', '5班'],
    '姓名': ['张三', '李四', '王五', '韩六', '赵七'],
    '性别': ['男', '男', '男', '女', '女'],
    '身高': [177, 151, 167, 175, 153],
    '语文成绩': [92, 84, 80, 77, 87],
    '学分': [1.5, 2.3, 3.2, 1.2, 1.8],
    '日期': ['2019/3/23', '2019/3/24', '2019/3/25', '2019/3/26', '2019/3/27']
}
df = pd.DataFrame(data)

# 按照班级和性别分组 统计每个分组的人数
df1 = df.groupby(by=['班级', '性别'], as_index=False)['学号'].count()
print(df1)

# 按照班级和性别分组 统计每个分组的成绩
df2 = df.groupby(by=['班级', '性别'], as_index=False)['语文成绩'].mean()
print(df2)
