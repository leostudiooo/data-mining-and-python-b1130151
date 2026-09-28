"""
本关任务：第一行输入圆的半径（圆心为原点），第二行输入坐标系某个点的横坐标和纵坐标，判断该点在圆内、圆上或圆外，并输出指定结果

提示：半径和坐标均为浮点类型数据，判断是否在圆上时不能直接使用==，而应该判断距离和半径的差是否足够小（本题假设阈值为1e-6）

测试输入：
2
2 0
预期输出：在圆上

测试输入：
2
1 0
预期输出：在圆内
"""

radius = float(input())
x, y  = map(float, input().split())

# 开始补充代码，输出格式必须和样例一致

EPSILON = 1e-6

distance_from_origin = (x ** 2 + y ** 2) ** 0.5

if abs(distance_from_origin - radius) < EPSILON:
    print("在圆上")
elif distance_from_origin < radius:
    print("在圆内")
else:
    print("在圆外")