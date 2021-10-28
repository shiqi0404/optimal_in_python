# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python
File Name：     demo5_numpy solver
Description :   Numpy 求解 线性代数

                x - 2*y + z = 0
                2*y - 8*z - 8 =0
                -4*x + 5*y + 9*z +9 =0

                按照 AX + b = 0 的形式整理

                A = [[1, -2, 1],    b = [0, -8. 9]
                     [0, 2, -8],
                     [-4, 5, 9]]

Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 19:29
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
# Numpy求解线性代数
import numpy as np

A = np.array([[1, -2, 1],
              [0, 2, -8],
              [-4, 5, 9]])
B = np.array([0, -8, 9])

result = np.linalg.solve(A, B)
print('x=', result[0])
print('y=', result[1])
print('z=', result[2])
# x= -29.0
# y= -16.0
# z= -3.0


