# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo1_base
Description :   Gurobi 中的数据结构:
                1.Multidict;
                2.Tuplelist;
                3.Tupledict;
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-10-28 23:09
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-10-28:
-------------------------------------------------
"""
import gurobipy as grb

# multidict 用法
student, chinese, math, english = grb.multidict(
    {
        'student1': [1, 2, 3],
        'student2': [2, 3, 4],
        'student3': [3, 4, 5],
        'student4': [4, 5, 6],
    }
)

print('student:', student)  # ['student1', 'student2', 'student3', 'student4']
print('chinese:', chinese)  # {'student1': 1, 'student2': 2, 'student3': 3, 'student4': 4}
print('math:', math)  # {'student1': 2, 'student2': 3, 'student3': 4, 'student4': 5}
print('english:', english)  # {'student1': 3, 'student2': 4, 'student3': 5, 'student4': 6}
