# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   gurobi 
File Name：     demo2_7
Description :   类与实例
                类 是面向对象编程很重要的概念。 类 由 属性 和 方法 组成。
                例 小猫 是一个 类， 其属性包含 毛色、体重，方法包括 抓老鼠。
                   学生 是一个 类， 其属性包含 学号、身高、体重等，方法包括 学生能干什么，包括学习、考试等。
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-11-26 17:14
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-11-26:
-------------------------------------------------
"""


# 定义一个类
def catch_mice():
    """"抓老鼠的方法"""
    print('抓老鼠')


class cat:
    def __init__(self, color, weight):  # 第一个参数是self，不可改变 !! 这里 init 不是 int 且 前后两个下划线
        self.color = color
        self.weight = weight

    def eat_mice(self):
        """吃老鼠"""
        print('吃老鼠')


# 类的实例化
my_cat = cat('yellow', 10)

# 调用类的方法
catch_mice()  # 输出 抓老鼠
my_cat.eat_mice()  # 输出 吃老鼠

# 查看类的属性
print(my_cat.color)  # 输出 yellow
print(my_cat.weight)  # 输出 10
