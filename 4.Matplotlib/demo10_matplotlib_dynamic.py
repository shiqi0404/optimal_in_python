# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo10_matplotlib_dynamic
Description :   绘制动态图
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 19:42
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


class car:  # 定义一个类
    def __init__(self, marker):
        self.x = 1
        self.y = 1
        self.marker = marker

    def move(self):  # 东西南北随机走一步
        self.x = self.x + np.random.randint(low=-1, high=2, size=1)[0]
        self.y = self.y + np.random.randint(low=-1, high=2, size=1)[0]
        # 设置边界
        self.x = self.x if self.x > 0 else 0
        self.x = self.x if self.x < 10 else 10
        self.y = self.y if self.x > 0 else 0
        self.y = self.y if self.x < 10 else 10


cars = [car(marker='o'), car(marker='^'), car(marker='*')]

fig = plt.figure()  # 绘制画布

i = list(range(1, 1000))  # 模拟1000个点


# 更新函数 在每个时间点操作图像对象
def update(i):
    plt.clf()  # 清空图层
    for c in cars:
        c.move()  # 移动1步
        x = c.x
        y = c.y
        marker = c.marker
        plt.xlim(0, 10)  # 限制图形区域
        plt.ylim(0, 10)
        plt.scatter(x, y, marker=marker)  # 绘制卡车
    return


ani = animation.FuncAnimation(fig, update)
plt.show()
