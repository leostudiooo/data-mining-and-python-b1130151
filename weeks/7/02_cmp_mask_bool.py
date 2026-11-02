"""
任务描述

本关任务：编写一个能比较并筛选数据的程序。

相关知识

为了完成本关任务，你需要掌握：

比较；
布尔数组作掩码；
布尔逻辑。
比较

在许多情况下，数据集可能不完整或因无效数据的存在而受到污染。我们要基于某些准则来抽取、修改、计数或对一个数组中的值进行其他操作时，就需要掩码了。接下来将学习如何用 布尔掩码 来查看和操作数组中的值。

和算术运算符一样，比较运算符在 numpy 中也是通过通用函数来实现的。比较运算符和其对应的通用函数如下：

比较运算符	通用函数
==	np.equal
!=	np.not_equal
<	np.less
<=	np.less_equal
>	np.greater
>=	np.greater_equal
这些比较运算符通用函数可以用于任意形状、大小的数组。示例如下：

data=np.array([('Alice', 4, 40),('Bob', 11, 85.5),('Cathy', 7, 68.0),('Doug', 9, 60)],dtype=[
              ("name","S10"),("age","int"),("score","float")])  #构造结构化数组
print(data["age"]<10)
'''
输出：array([ True, False,  True,  True])
'''
print(data["score"]>60)
'''
输出:array([False,  True,  True, False])
'''
print(data["score"]>=60)
'''
输出:array([False,  True,  True,  True])
'''
print(data["score"]<=60)
'''
输出:array([ True, False, False,  True])
'''
print(data["age"]!=9)
'''
输出:array([ True,  True,  True, False])
'''
print((data["age"]/2)==(np.sqrt(data["age"])))
'''
输出:array([ True, False, False, False])
'''
布尔数组作掩码

一种更加强大的模式是使用布尔数组作为掩码，通过该掩码选择数据的子数据集，实现一些操作：

data=np.array([('Alice', 4, 40), ('Bob', 11, 85.5) ,('Cathy', 7, 68.0),
              ('Doug', 9, 60)],dtype=[("name","S10"),("age","int"),("score","float")])
 print(data)
'''
输出：[(b'Alice',  4, 40. )
(b'Bob', 11, 85.5)
(b'Cathy',  7, 68. )
 (b'Doug',  9, 60. )]
'''
 print(data["score"]>60)  #使用比较运算得的一个布尔数组
'''
输出:[False  True  True False]
'''
 print(data[data["score"]>60])  #进行简单的索引，即掩码操作将值为True的选出
'''
输出:[(b'Bob', 11, 85.5) (b'Cathy',  7, 68. )]
'''
布尔逻辑

结合 Python 的逐位逻辑运算符一起使用。逻辑运算符对应 numpy 中的通用函数如下表：

逻辑运算符	通用函数
&	np.bitwise_and
|	np.bitwise_or
^	np.bitwise_xor
~	np.bitwise_not
print(np.count_nonzero(data["age"]<10))#统计数组中True的个数
'''
输出:3
'''
#还可以用np.sum(),输出结果和count_nonzero一样,sum()的好处是可以沿着行或列进行求和
print(np.sum(data["age"]<10))
print(np.any(data["score"]<60))#是否有不及格的
'''
输出：True
'''
print(np.all(data["age"]>10))#是否都大于10岁
'''
输出:False
'''
print(data[data["age"]>10])#打印年龄大于10的信息
'''
输出：array([(b'Bob', 11, 85.5)],
      dtype=[('name', 'S10'), ('age', '<i4'), ('score', '<f8')])
'''
编程要求

根据提示，在右侧编辑器 Begin-End 部分补充代码，根据输入的数据筛选出大于 num 的值。

具体要求请参见后续测试样例。
请先仔细阅读右侧上部代码编辑区内给出的代码框架，再开始你的编程工作！

测试说明

平台会对你编写的代码进行测试，对比你输出的数值与实际正确的数值，只有所有数据全部计算正确才能进入下一关。

测试输入：
[[ 3 ,15, 9 ,11 , 7],[ 2, 0 , 8, 19 ,16],[ 6 , 6, 16 , 9, 5],[ 7 , 5 , 2 , 6 ,13]] 10

预期输出：
[15 11 19 16 16 13]
"""

import numpy as np


def student(num, input_data):
    result = []
    # ********* Begin *********#
    data = np.array(input_data)
    result = data[data > num]
    # ********* End *********#
    return result


if __name__ == '__main__':
    input_data = [[3, 15, 9, 11, 7], [2, 0, 8, 19, 16],
	    [6, 6, 16, 9, 5], [7, 5, 2, 6, 13]]
    num = 10
    expected_output = [15, 11, 19, 16, 16, 13]
    print(student(num, input_data) == expected_output)
