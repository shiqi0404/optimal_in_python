# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   optimal_in_python 
File Name：     demo1
Description :   
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2021-11-02 18:56
Software:       PyCharm
-------------------------------------------------
 Change Activity:
 2021-11-02:
-------------------------------------------------
"""
import gurobipy as grb

model = grb.Model()

x1 = model.addVars(vtype=grb.GRB.INTEGER, name="x1")
x2 = model.addVars(vtype=grb.GRB.INTEGER, name="x2")

model.addConstrs(2 * x1 + 3 * x2 <= 14)
model.addConstrs(4 * x1 + 2 * x2 <= 18)
model.addConstrs(x1 >= 0)
model.addConstrs(x2 >= 0)

model.setObjective(3 * x1 + 2 * x2, sense=grb.GRB.MAXIMIZE)

model.optimize()
print("objVal:", model.objVal)
for v in model.getVars():
    print("参数：", v.varName, '=', v.x)
