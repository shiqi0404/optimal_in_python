# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo6_pandas_apply
Description :   apply函数 对目标集合中的每个元素执行相同的操作
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 18:33
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


# apply
# 1. 姓名 每个元素都添加“xm”
def myfuc(x):
    return 'xm' + x


df['姓名'] = df['姓名'].apply(myfuc)
print(df)


# 2. 成绩小于90的，改为90
def myfunc1(x):
    if x < 90:
        return 90
    else:
        return x


df['语文成绩'] = df['语文成绩'].apply(myfunc1)
print(df)


# 3. 分组使用 apply
def myfunc2(series):
    return series.max()


df = df.groupby(by=['班级'], as_index=False)['语文成绩'].apply(myfunc2)
print(df)
