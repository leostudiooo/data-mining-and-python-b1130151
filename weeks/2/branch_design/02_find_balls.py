"""
本关任务：输入三个小球A B C的质量，其中必须有两个小球质量相同且与第三个球不同，输出质量不同的小球名字

测试输入：1 1 3
预期输出：C

测试输入：1 3 1
预期输出：B
"""

A, B, C = map(int, input().split())

# 开始补充代码，输出格式必须和样例一致

if A == B and A != C:
	print("C")
elif A == C and A != B:
	print("B")
elif B == C and B != A:
	print("A")