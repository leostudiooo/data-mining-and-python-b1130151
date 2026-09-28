"""
本关任务：输入正整数n，找出所有小于等于n，且是7的倍数，且个位数为4的数字的总和，输出该总和。

测试输入：100
预期输出：98
"""

n = int(input())

# 开始补充代码，求满足条件的数字之和

result = 0

for i in range(1, n + 1):
	if i % 7 == 0 and i % 10 == 4:
		result += i

print(result)