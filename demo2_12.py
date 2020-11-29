# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo2_12
Description :   Numpy 的矩阵运算
                利用 array 数组来模拟矩阵运算
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 19:10
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""
# Numpy 的矩阵运算
import numpy as np

a1 = np.array([[4, 5, 6], [1, 2, 3]])
a2 = np.array([[6, 5, 4], [3, 2, 1]])

# 矩阵相乘，即对应元素相乘
print('相乘:\n', a1 * a2)
# [[24 25 24]
#  [ 3  4  3]]

# 矩阵点乘，每个元素都乘以一个数
print('点乘:\n', a1 * 3)
# [[12 15 18]
#  [ 3  6  9]]

# 矩阵相乘，a1 和 a2 的维度为(2,3)*(2,3)维度不对应 则需要先对 a2 转置
a3 = a2.T   # 转置 操作
print('维度不同相乘:\n', np.dot(a1, a3))
# [[73 28]
#  [28 10]]

# 矩阵转置
print('a1转置:\n', a1.T)
# [[4 1]
#  [5 2]
#  [6 3]]

# 矩阵求逆
a = np.array([[1, 2, 3], [4, 5, 6], [5, 4, 3]])
print('矩阵a的逆:\n', np.linalg.inv(a))
# [[-8.44424930e+15  5.62949953e+15 -2.81474977e+15]
#  [ 1.68884986e+16 -1.12589991e+16  5.62949953e+15]
#  [-8.44424930e+15  5.62949953e+15 -2.81474977e+15]]

# 特征值与特征向量
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
eigenValues, eigVector = np.linalg.eig(b)
print('矩阵b的特征值:\n', eigenValues)
# [ 1.61168440e+01 -1.11684397e+00 -9.75918483e-16]
print('矩阵b的特征向量:\n', eigVector)
# [[-0.23197069 -0.78583024  0.40824829]
#  [-0.52532209 -0.08675134 -0.81649658]
#  [-0.8186735   0.61232756  0.40824829]]

# SVD 奇异值分解
U, sigma, V = np.linalg.svd(b, full_matrices=False)
print('U:\n', U)
# [[-0.21483724  0.88723069  0.40824829]
#  [-0.52058739  0.24964395 - 0.81649658]
#  [-0.82633754 - 0.38794278 0.40824829]]
print('sigma:\n', sigma)
# [1.68481034e+01 1.06836951e+00 3.33475287e-16]
print('V:\n', V)
# [[-0.47967118 - 0.57236779 - 0.66506441]
#  [-0.77669099 - 0.07568647  0.62531805]
#  [-0.40824829   0.81649658 - 0.40824829]]

# 矩阵的行列式
det = np.linalg.det(b)
print('矩阵b的行列式: ', det)
# -9.51619735392994e-16

# QR分解
Q,R = np.linalg.qr(b)
print('Q: \n', Q)
# [[-0.12309149  0.90453403  0.40824829]
#  [-0.49236596  0.30151134 - 0.81649658]
# [-0.86164044 - 0.30151134  0.40824829]]
print('R: \n', R)
# [[-8.12403840e+00 - 9.60113630e+00   - 1.10782342e+01]
#  [0.00000000e+00    9.04534034e-01     1.80906807e+00]
#  [0.00000000e+00    0.00000000e+00   - 1.11164740e-15]]

