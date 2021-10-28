# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo3_pandas_statics
Description :   Pandas 中基础统计函数
            count           计数
            min max         最小 最大
            argmin argmax   最小 最大的索引位置
            idxmin idxmax   最小 最大值的索引值
            quantile        计算样本分位数
            sum mean        求和 均值
            meidam          中位数
            var cov         方差 标准差
            cumsum          累计和
            cummins cummax  累计最小 最大
            cumprod         累计积
            diff            一阶差分
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 12:25
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""

# DataFrame 表格数据 1
import pandas as pd

df = pd.DataFrame(data={
    '学号': ['x1', 'x2', 'x3', 'x4', 'x5'],
    '姓名': ['张三', '李四', '王五', '韩六', '赵七'],
    '身高': [177, 151, 167, 175, 153],
    '语文成绩': [92, 84, 80, 77, 87],
    '学分': [1.5, 2.3, 3.2, 1.2, 1.8],
    '日期': ['2019/3/23', '2019/3/24', '2019/3/25', '2019/3/26', '2019/3/27']
})

print('表格数据：\n')
print(df)

# 查看DataFrame的维度
print('\nDataFrame维度： ', df.shape)  # DataFrame维度：  (5, 6)

# 从DataFrame拆分出一个Series ： DataFrame中的一列就是一个Series
high = df['身高']
print(high)
# 输出
# 0    177
# 1    151
# 2    167
# 3    175
# 4    153
# Name: 身高, type: int64

# Max and Min
df_max = df['身高'].max()  # 177
df_min = df['身高'].min()  # 151

# Mean and Std
df_mean = df['身高'].mean()  # 164.6
df_std = df['身高'].std()  # 12.116104984688768

# 90% 分位数
df_quantile = df['身高'].quantile(q=0.9)  # 176.2

# print(df_max, df_min, df_mean, df_std, df_quantile)

# 累加值
df_sumall = df['身高'].cumsum()
# print(df_sumall)
# 0    177
# 1    328
# 2    495
# 3    670
# 4    823
# Name: 身高, dtype: int64

# 相关系数
df_corr = df[['身高', '语文成绩']].corr(method='pearson')
# print(df_corr)
#             身高      语文成绩
# 身高    1.000000 -0.063232
# 语文成绩 -0.063232  1.000000

# 协方差
df_cov = df[['身高', '语文成绩']].cov()
# print(df_cov)
#          身高  语文成绩
# 身高    146.8  -4.5
# 语文成绩   -4.5  34.5

