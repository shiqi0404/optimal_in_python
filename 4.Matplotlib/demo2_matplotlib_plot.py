# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo2_matplotlib_plot
Description :   绘制折线图
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 19:06
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

x = np.linspace(start=0, stop=30, num=300)
y = np.sin(x)
plt.plot(x, y, color='r', marker='d', linestyle='--', linewidth=1.5, alpha=0.8)
# 红色 菱形点 虚线 线宽1.5 透明度0.8
plt.title('折线图')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
