# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo3_matplotlib_bar
Description :   绘制条形图（柱状图）
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 19:07
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

x = ['a', 'b', 'c', 'd']
y = [3, 5, 7, 9]
plt.bar(x, y, width=0.5)
plt.title('柱状图')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
