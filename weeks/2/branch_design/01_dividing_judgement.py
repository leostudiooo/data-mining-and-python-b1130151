"""
本关任务：编写任意整数被3和5整除的情况。
如果都能，则输出A
如果只能被3整除，则输出B
如果只能被5整除，则输出C
如果都不能整除，则输出D

测试输入：4
预期输出：D

测试输入：15
预期输出：A
"""

number = int(input())

# 开始补充代码，根据样例要求输出对应结果

if number % (3 * 5) == 0:
    print("A")
elif number % 3 == 0:
    print("B")
elif number % 5 == 0:
    print("C")
else:
    print("D")