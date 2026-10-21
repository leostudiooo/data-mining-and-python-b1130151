"""
任务描述

据说著名历史学家 Josephus有过以下的故事：Josephus及他的朋友共41人围成一个圆圈，由第1个人开始报数，每数到3该人就必须出去，然后再由下一个人重新报数，直到圆圈上少于3人为止。Josephus 将朋友与自己安排在第16个与第31个位置，成为最后剩下的人。
扩展这个问题，当人数为n，每次报数为k时，求解最后的K-1个剩下的人的位置

输入格式
在同一行内输入两个正整数n和k，要求k > = 2且n >= k

输出格式
以列表形式显示剩余的人的序号。
如果k<2或者n<k,打印Data Error!

示例 1
输入：
41 3

输出：
[16, 31]

平均代码量 11 行
"""

n, k = map(int, input().split())

if k < 2 or n < k:
	print("Data Error!")
else:
	people = list(range(1, n + 1))
	index = 0
	while len(people) >= k:
		index = (index + k - 1) % len(people)
		people.pop(index)
	print(people)