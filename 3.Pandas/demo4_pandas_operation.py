# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo4_pandas_operation
Description :   针对DataFrame数据进行数据处理
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
import numpy as np
import pandas as pd

df = pd.DataFrame(data={
    '学号': ['x1', 'x2', 'x3', 'x4', 'x5'],
    '姓名': ['张三', '李四', '王五', '韩六', '赵七'],
    '身高': [177, 151, 167, 175, 153],
    '语文成绩': [92, 84, 80, 77, 87],
    '学分': [1.5, 2.3, 3.2, 1.2, 1.8],
    '日期': ['2019/3/23', '2019/3/24', '2019/3/25', '2019/3/26', '2019/3/27']
})

# 重命名列表

df = df.rename(columns={'语文成绩': '成绩'})
# print(df)

# 添加列
df['新列名1'] = [1, 2, 3, 4, 5]  # 添加新数据
df['新列名2'] = df['成绩'] * 0.8  # 基于原数据计算
# print(df)

# 删除列
df = df.drop(columns=['新列名2'])  # 删除方法1
# print(df)
del df['新列名1']  # 删除方法2
# print(df)

# 子集选择
"""
应用 loc / iloc 函数，
loc读取的是索引；
iloc读取的是行数，相当于重新命名索引维0,1,2,...
"""
df1 = df.loc[2:4]
print(df1)

df2 = df.iloc[1:4]
print(df2)

# 读取满足条件数据
df3 = df.loc[(df['身高'] > 160) & (df['成绩'] > 80), ['姓名', '学分', '日期']]
print(df3)

# 排序 根据成绩降序排序， ascending = True 表示升序 False 表示降序
df4 = df.sort_values(by=['成绩'], ascending=False)
print(df4)

# 缺失值处理
# 缺失值使用 fillna 填充
# 1.先设置成NaN 然后用固定值(80)填充
df.loc[(df['姓名'] == '张三'), '成绩'] = np.NaN
# df['成绩'] = df['成绩'].fillna(80)

# 2.用均值填充缺失值
df['成绩'] = df['成绩'].fillna(df['成绩'].mean())
# print(df)

# 异常值处理
# 将大于“均值+2倍标准差”认定为异常值，用“均值+2倍标准差替代异常值”
abnormal = df['成绩'].mean() + 2 * df['成绩'].std()
print(abnormal)
df.loc[df['成绩'] > abnormal, '成绩'] = abnormal
print(df)

# 删除重复记录
# 根据“姓名 学号”判断是否重复，若重复则删除重复记录，只保留一条记录
df = df.drop_duplicates(subset=['姓名', '学号'])
print(df)
