"""
本关任务：输入一个大写字母（如A），在第一行输出大写字母本身和ASCII码值，第二行输出对应的小写字母和其ASCII值
注意输出内容的格式必须符合示例要求


通过ord函数和chr函数进行操作，输出时可以使用格式化字符串

测试输入：
A

预期输出：
A, 65
a, 97
"""

ch = input() # 输入一个大写字母

# 开始补充代码
difference = ord('A') - ord('a')

print(ch + ", " + str(ord(ch)))
print(chr(ord(ch) - difference) + ", " + str(ord(ch) - difference))

# 结束补充代码
