# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo7_matplotlib_3Dscatter
Description :   绘制三维散点图
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 19:31
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')  # 指定为3D

x1 = np.random.random(100) * 20
y1 = np.random.random(100) * 20
z1 = x1 + y1
ax.scatter(x1, y1, z1, c='r', marker='o')

x2 = np.random.random(100) * 20
y2 = np.random.random(100) * 20
z2 = x2 + y2
ax.scatter(x2, y2, z2, c='b', marker='^')

plt.show()
