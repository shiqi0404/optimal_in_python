# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python
File Name：     demo1_Ortools
Description :   Ortools 求解线性规划模型

                min Z = 5*x1 + 6*x2 + 23*x3 + 5*x4 + 24*x5 + 6*x6 +23*x7 + 5*x8
                s.t. 2*x1 + x2 + x3 + x4 >= 100
                     2*2 + x3 + 3*x5 + 2*x6 + x7 >= 150
                     x1 + x3 + 3*x4 + 2*x6 + 3*x7 + 5*x8 >= 100
                     x1, x2, ... , x8 >=0 且为整数

Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-23 17:21
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-23:
-------------------------------------------------
"""

from ortools.sat.python import cp_model

model = cp_model.CpModel()

# 定义变量
x1 = model.NewIntVar(0, 1000, 'x1')
x2 = model.NewIntVar(0, 1000, 'x2')
x3 = model.NewIntVar(0, 1000, 'x3')
x4 = model.NewIntVar(0, 1000, 'x4')
x5 = model.NewIntVar(0, 1000, 'x5')
x6 = model.NewIntVar(0, 1000, 'x6')
x7 = model.NewIntVar(0, 1000, 'x7')
x8 = model.NewIntVar(0, 1000, 'x8')

# 添加约束
model.Add(2 * x1 + x2 + x3 + x4 >= 100)
model.Add(2 * 2 + x3 + 3 * x5 + 2 * x6 + x7 >= 150)
model.Add(x1 + x3 + 3 * x4 + 2 * x6 + 3 * x7 + 5 * x8 >= 100)

# 添加目标函数
model.Minimize(5 * x1 + 6 * x2 + 23 * x3 + 5 * x4 + 24 * x5 + 6 * x6 + 23 * x7 + 5 * x8)

# 求解
solver = cp_model.CpSolver()
solver.Solve(model)

print('目标函数值是: ', solver.ObjectiveValue())
print('x1 = ', solver.Value(x1))
print('x2 = ', solver.Value(x2))
print('x3 = ', solver.Value(x3))
print('x4 = ', solver.Value(x4))
print('x5 = ', solver.Value(x5))
print('x6 = ', solver.Value(x6))
print('x7 = ', solver.Value(x7))
print('x8 = ', solver.Value(x8))
