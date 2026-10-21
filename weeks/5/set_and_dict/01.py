"""
任务描述

输入一个非空字符串，去除重复的字符后，从小到大排序输出为一个新字符串。

输入格式

一个非空字符串

输出格式

去重排序后的字符串

示例

输入：
Life is short, you need Python!
输出：
!,LPdefhinorstuy
"""

s = input()
s = sorted(set(s))
print(''.join(s))