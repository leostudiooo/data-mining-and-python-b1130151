"""
本关任务：输入正整数n，求1至n的阶乘之和，即求解1! + 2! + ... + n!

测试输入：5
预期输出：153
"""

n = int(input())

# 开始补充代码，求1至n的阶乘总和

result = 0

for i in range(1, n + 1):
	factorial = 1
	for j in range(1, i + 1):
		factorial *= j
	result += factorial

print(result)