# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo9_matplotlib_3Dsurface
Description :   
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 19:34
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')  # 指定为3D

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)  # np.meshgrid 生成坐标网格矩阵
z = np.sin(np.sqrt(x ** 2 + y ** 2))

surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)
# cmap=cm.coolwarm 颜色属性
plt.show()
