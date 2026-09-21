"""
本关任务：一只大象口渴了，要喝20升水才能解渴，但现在只有一个深h厘米，底面半径为r厘米的小圆桶(假设h和r都是整数)。问大象至少要喝多少桶水才会解渴。
要求：输入h和r的值，输出最后的结果

测试输入：
23
11

预期输出：
3
"""

from math import pi as PI
from math import ceil

height = float(input(''))  # 输入圆桶的高
radius = float(input(''))  # 输入圆桶的半径

# 开始补充代码，格式必须和样例一致

VOLUME_NEEDED = 20.0 * 1e3 # Liters to cm3

def calc_volume(radius_, height_):
	return PI * radius_ ** 2 * height_

num_buckets = ceil(VOLUME_NEEDED / calc_volume(radius, height))
print(num_buckets)