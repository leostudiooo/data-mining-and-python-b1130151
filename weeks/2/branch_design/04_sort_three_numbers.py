"""
本关任务：输入三个整数，按从小到大的顺序依次输出这三个数，每两个数之间用空格分隔

测试输入：1 2 3
预期输出：1 2 3

测试输入：3 2 1
预期输出：1 2 3
"""

a, b, c = map(int, input().split())

# 开始补充代码，输出格式必须和样例一致

if a <= b and a <= c:
	if b <= c:
		print(a, b, c)
	else:
		print(a, c, b)
elif b <= a and b <= c:
	if a <= c:
		print(b, a, c)
	else:
		print(b, c, a)
else:
	if a <= b:
		print(c, a, b)
	else:
		print(c, b, a)