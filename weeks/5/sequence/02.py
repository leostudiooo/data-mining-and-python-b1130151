"""
相关知识

推导式可以从一个数据序列构建另一个新的数据序列的结构体。本质上可以将其理解成一种集合了变换和筛选功能的函数，通过这个函数把一个序列转换成另一个序列。
共有三种推导式：
列表(list)推导式
字典(dict)推导式
集合(set)推导式
列表推导式是一种创建新列表的便捷的方式，通常用于根据一个列表中的每个元素通过某种运算或筛选得到另外一系列新数据，创建一个新列表。 列表推导式由1个表达式跟一个或多个for 从句、0个或多个if从句构成。

# 列表推导式由1个表达式跟一个或多个for 从句、0个或多个if从句构成。
# 列表推导式置于一对方括号之中
[x**2 for x in range(10)]  #计算range(10)中每个数的平方，推导出新列表
# 得到新列表[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
for前面是一个表达式，in 后面是一个列表或能生成列表的对象。将in后面列表中的每一个数据作为for前面表达式的参数，再将计算得到的序列转成列表。if是一个条件从句，可以根据条件返回新列表。
for前面也可以是一个内置函数或自定义函数，例如：

 # 自定义函数f(x)
def fun(x):
    return x + x ** 2 + x ** 3
     # 返回 x + x ** 2 + x ** 3
y = [fun(i) for i in range(10)]    # 列表推导式，按函数fun(x)，推导出新列表
print(y)                           # 输出列表[0, 3, 14, 39, 84, 155, 258, 399, 584, 819]
列表推导式还可以用条件语句（if从句）对数据进行过滤，用符合特定条件的数据推导出新列表，例如：

def fun(x):
    return x + x ** 2 + x ** 3
# 返回x + x ** 2 + x ** 3
# 列表推导式，根据原列表中的偶数，推导新列表
y = [fun(i) for i in range(10) if i % 2 == 0]
print(y)  # 输出列表[0, 14, 84, 258, 584]
可以用多个for从句对多个变量进行计算，例如：

 ls = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(ls)      # 输出[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
列表推导式应用实例

 ls = [-4, -2, 0, 2, 4]
print([x*2 for x in ls])# 将原列表每个数字乘2，推导出新列表 [-8, -4, 0, 4, 8]
print([x for x in ls if x >= 0])   # 过滤列表，返回只包含正数的列表[0, 2, 4]
print([abs(x) for x in ls])        # 应用abs()函数推导新列表[4, 2, 0, 2, 4]
# 调用strip()方法去除每个元素前后的空字符,返回['banana', 'apple', 'pear']
freshfruit = ['  banana', '  apple ', 'pear  ']
print([fruit.strip() for fruit in freshfruit]) #
# 生成一个每个元素及其平方(number, square)构成的元组组成的列表
print([(x, x**2) for x in range(6)]) 
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
将列俩表推导式的[]改成()即可得到生成器

 print([x ** 3 for x in range(10)])
# 输出列表 [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print((x ** 3 for x in range(10)))
# 输出生成器对象 <generator object <genexpr> at 0x000001FBC47185C8>
print(list(x ** 3 for x in range(10)))
# 生成器可遍历或转列表
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
字典推导和列表推导的使用方法是类似的，只是中括号该改成大括号。

 dic = {'李明': '20191202001', '张凡':'20191202002'} # 姓名：学号
dic_update = {v: k for k, v in dic.items()}
print(dic_update)
# 输出交换了键和值的字典 {'20191202001': '李明', '20191202002': '张凡'}
集合推导式跟列表推导式也是类似的， 唯区别在于它使用大括号{}。

 print({x ** 3 for x in range(10)})
# 输出集合 {0, 1, 64, 512, 8, 343, 216, 729, 27, 125}
实验任务描述
现有一列表 ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']，编写程序，实现以下功能：
输入“1”，输出元素为0-9的3次方的列表
输入“2”，输出元素为0-9中偶数的3次方的列表
输入“3”，输出元素为元组的列表，元组中元素依次是0-9中的奇数和该数的3次方
输入“4”，将列表 ls 中每个元素首字母转为大写字母，输出新列表str.capitalize()函数可以将字符串str的首字母转换为大写字母。

输入其他字符，输出“结束程序”

展实践
在自己电脑上编程，对生成器进行遍历输出，了解生成器成列表推导式的异同。

示例
输入：
1

输出：[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
平均代码量 13 行
"""

ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']
selection = input()

if selection == "1":
	print([i ** 3 for i in range(10)])
elif selection == "2":
	print([i ** 3 for i in range(0, 10, 2)]) # even numbers
elif selection == "3":
	print([(i, i ** 3) for i in range(1, 10, 2)]) # odd numbers, tuples
elif selection == "4":
	print([s.capitalize() for s in ls])
	# or
	print(list(map(str.capitalize, ls)))
else:
	print("结束程序")