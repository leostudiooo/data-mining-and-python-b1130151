"""
本关任务：使用input函数输入圆柱体的高和半径，输出圆柱体的全面积和体积。

圆周率从math当中导入pi常量实现
输出结果时，全面积和体积只保留小数点后两位（使用格式字符串当中的.2f实现）

平台会对你编写的代码进行测试：

测试输入：
4
5

预期输出：
全面积是282.74
体积是314.16
"""

from math import pi as PI

height = float(input(''))  # 输入圆柱体的高
radius = float(input(''))  # 输入圆柱体的半径

# 开始补充代码，格式必须和样例一致

def calc_surface_area(radius_, height_):
	return PI * radius_ * (2 * height_ + 2 * radius_)

def calc_volume(radius_, height_):
	return PI * radius_ ** 2 * height_

print(f'全面积是{calc_surface_area(radius, height):.2f}')
print(f'体积是{calc_volume(radius, height):.2f}')