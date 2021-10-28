# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo1_matplotlib_scatter
Description :   绘制散点图
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 18:57
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示图像中的负号

x = np.random.randint(low=2, high=10, size=10)
y = np.random.randint(low=2, high=10, size=10)
plt.scatter(x, y)
plt.title('散点图')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
