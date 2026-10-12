"""
任务描述
输入一个1000以内的正整数 n,在同一行内输出 [0,n] 之间各位数字之和为5的数，数字之间用空格分开（行末有一个空格）。

输入格式
输入一个1000以内的正整数 n

输出格式
在一行内依次输出所有符合条件的数，数字之间用空格分开（行末有一个空格）

示例
输入：
100

输出：
5 14 23 32 41 50
"""

range_end = int(input())
result = []
for i in range(range_end + 1):
	if sum(int(digit) for digit in str(i)) == 5:
		result.append(str(i))
print(" ".join(result) + " ")