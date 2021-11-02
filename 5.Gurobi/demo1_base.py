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

'''
1. Multidict 用法
复合字典（多重字典）
允许一个语句中初始化一个或多个字典
'''
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

'''
2. Tuplelist 用法
元组列表，tuple和list的组合，list的元素是tuple的类型
'''
tl = grb.tuplelist([(1, 2), (1, 3), (2, 3), (2, 5)])

print('第一个值是1的元素:\n', tl.select(1, '*'))
print('第二个值是3的元素:\n', tl.select('*', 3))

tl.append((3, 5))  # 添加元素
print(tl.select(3, '*'))

print(tl.select(1, '*'))  # 迭代的方法 实现 select
'''
tuplelist 基本和 list 一样，Gurobi添加了select方法， tuplelist 可以看作list对象 
'''

'''
3. Tupledict
属于Python的dict的子类，tupledict内置方法可以高效构建线性表达式，sum / prod
'''
# model = grb.Model()
#
# t2 = [
#     (1, 1), (1, 2), (1, 3),
#     (2, 1), (2, 2), (2, 3),
#     (3, 1), (3, 2), (3, 3)]
# vars1 = model.addVars(t2, name="d")
# #
# # print(sum(vars1.select(1, '*')))
#
# c1 = [(1, 1), (1, 2), (1, 3)]
# coeff = grb.tupledict(c1)
# coeff[(1, 1)] = 1
# coeff[(1, 2)] = 0.3
# coeff[(1, 3)] = 0.4
#
# print(vars1.prod(coeff, 1, '*'))
'''以上部分的结果与书中有差异，还需要进一步验证 '''
m = grb.Model()
x = m.addVars(3, 4, vtype=grb.GRB.BINARY, name="x")
m.addConstrs((x.sum(i, '*') <= 1 for i in range(3)), name="con")
m.update()
m.write("tupledict_vars.lp")
