# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo_operation
Description :   基础数据类型、基础四则运算、逻辑运算
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 15:37
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""

# 基础数据类型
int_a = 1   # 整数变量，即数学中的整数
float_b = 1.2   # 浮点数变量， 即数学中的小数
bool_t = True   # 布尔值中的真
bool_f = False  # 布尔值中的假
str_c = "abc"   # 字符串变量，使用双引号

# 基础四则运算
a = 1
b = 2
print('加法: a + b = ', a + b)
print('减法: a - b = ', a - b)
print('乘法: a * b = ', a * b)
print('除法: a / b = ', a / b)
print('取余: a % b = ', a % b)
print('四则运算: (a + b)/(a * b)', (a + b)/(a * b))

# 数学中的逻辑运算
print('(a > 0) or (b > 3): ', a > 0 or b > 3)       # 逻辑或，结果为真
print('(a > 0) and (b > 3): ', a > 0 and b > 3)     # 逻辑与，结果为假
print('not a > 0 : ', not a > 0)                    # 逻辑非，结果为假
