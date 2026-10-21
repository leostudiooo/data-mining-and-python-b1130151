"""
任务描述

费马大定理断言，当整数 n > 2时，关于 a,b,c 的方程a 
n
 = b 
n
  + c 
n
  没有正整数解。 该定理被提出来后，历经三百多年，经历多人猜想辩证，最终在 1995 年被英国数学家安德鲁.怀尔斯证明。 
不过，可以找到大于 1 的 4 个整数满足完美立方等式：
a 
3
  = b 
3
  + c 
3
  + d 
3
  
(例如 12 
3
  = 6 
3
  + 8 
3
  + 10 
3
 ) 
编写一个程序，对于任意给定的正整数 N（N<=100），寻找所有的四元组（a,b,c,d），满足 
a 
3
  = b 
3
  + c 
3
  + d 
3
   (其中 1 < a,b,c,d <=N)

输入格式
整数 N(1 < N <= 100)

输出格式
按照 a 的值从小到大，每行输出一个完美立方等式，其中b,c,d按照非降序排列输出。
（若两个完美立方式中 a 值相同，则 b 值小的先输出；在 b 值相等的情况下，c 值小的先输出，在 b,c 都相等的情况下，d 值小的先输出。）

示例
输入：
24
输出：
Cube = 6,Triple = (3,4,5)
Cube = 12,Triple = (6,8,10)
Cube = 18,Triple = (2,12,16)
Cube = 18,Triple = (9,12,15)
Cube = 19,Triple = (3,10,18)
Cube = 20,Triple = (7,14,17)
Cube = 24,Triple = (12,16,20)
平均代码量 8 行
"""

number_N = int(input())
for a in range(2, number_N + 1):
    a_cubed = a ** 3
    for b in range(2, number_N + 1):
        for c in range(b, number_N + 1):
            for d in range(c, number_N + 1):
                if a_cubed == b ** 3 + c ** 3 + d ** 3:
                    print(f"Cube = {a},Triple = ({b},{c},{d})")