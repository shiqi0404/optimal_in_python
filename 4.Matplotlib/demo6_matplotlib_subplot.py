# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo6_matplotlib_subplot
Description :   绘制子图
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 19:17
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

fig = plt.figure(figsize=(8, 8))  # 指定画布大小

ax1 = fig.add_subplot(2, 2, 1)  # 添加子图
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# 图1 Sin
x = np.linspace(start=0, stop=30, num=300)
y = np.sin(x)
ax1.plot(x, y)
ax1.set_title('Sin Plot')
ax1.grid()

# 图2 Scatter
x = np.random.randint(low=2, high=10, size=10)
y = np.random.randint(low=2, high=10, size=10)
ax2.scatter(x, y)
ax2.set_title('Scatter Plot')
ax2.grid()

# 图3 Hist
x = np.random.normal(loc=0, scale=1, size=1000)
ax3.hist(x=x, bins=50)
ax3.set_title('Hist Plot')
ax3.grid()

# 图4 Combination
# 图1 Sin
x1 = np.linspace(start=0, stop=30, num=300)
y1 = np.sin(x1)

x2 = np.random.randint(low=0, high=10, size=10)
y2 = np.random.randint(low=0, high=10, size=10) / 10
ax4.plot(x1, y1, color='b', label='line plot')
ax4.scatter(x2, y2, color='r', label='scatter plot')
ax4.set_title('Combination Plot')
ax4.grid()

plt.show()
