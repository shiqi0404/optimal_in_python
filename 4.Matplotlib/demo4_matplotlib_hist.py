# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo4_matplotlib_hist
Description :   
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 19:09
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

x = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(x)
plt.title('直方图')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
