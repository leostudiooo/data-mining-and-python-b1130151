"""
任务描述
本关任务：
计算特殊序列表达式的值，
a+aa+aaa+aaaa+...+a...a(N个a)
其中1<=a<=9，第N项由N个a组成.

例：若a=1,N=3，表达式为：
1+11+111

编程要求

输入：
第一行输入一个整数A，且该数应该介于1至9之间（包含1和9）
第二行输入一个整数N。

输出：
输出其 N 项数列之和的值。
当输入不符合要求时输出：data error

测试说明
测试输入：
1
3
预期输出：
123

测试输入：
12
-3
预期输出：
data error
"""

number_A_char = input()
number_N = int(input())

if int(number_A_char) < 1 or int(number_A_char) > 9 or number_N < 0:
    print("data error")
else:
    total_sum = 0
    current_term = ""
    for i in range(1, number_N + 1):
        current_term += number_A_char
        total_sum += int(current_term)
    print(total_sum)
