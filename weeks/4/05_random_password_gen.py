"""
任务描述
从字符串 '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\()*+,-.' 中每次随机抽取 1 个字符，重复 n 次，用取得的字符构成的一个新字符串用做密码，密码长度 n 和随机数种子 s 由用户输入。
本题必须使用random.choice()函数进行随机抽取

输入格式
在一行内输入2个正整数 n 和 s，分别表示密码长度和随机数种子，数字间用半角逗号分隔。

输出格式
一个长度为 n 字符串

示例
输入：
10,5

输出：
wJ&3Xv6keL
"""

import random

BASE_STRING = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\\()*+,-.'

length, seed = map(int, input().split(','))
random.seed(seed)
password = ''.join(random.choice(BASE_STRING) for _ in range(length))

print(password)