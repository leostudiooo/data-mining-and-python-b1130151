"""
本关任务：输入一个正整数n，求不超过n的正偶数之和并输出。
如输入10，则答案为2 + 4 + 6 + 8 + 10 = 30

测试输入：10
预期输出：30
"""

n = int(input())

# 开始补充代码，输出不超过n的正偶数之和

UPPER_BOUND = n if n % 2 == 0 else n - 1
result = 0

for i in range(2, UPPER_BOUND + 1, 2):
	result += i

print(result)