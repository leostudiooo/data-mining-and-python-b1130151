"""
任务描述

本关任务：利用广播机制实现 Z-score 标准化。

相关知识

为了完成本关任务，你需要掌握：

什么是广播；
广播的原则。
什么是广播

两个 ndarray 对象的相加、相减以及相乘都是对应元素之间的操作。

import numpy as np
x = np.array([[2,2,3],[1,2,3]])
y = np.array([[1,1,3],[2,2,4]])
print(x*y) 
'''
输入结果如下：
[[ 2  2  9]
 [ 2  4 12]]
'''
当两个 ndarray 对象的形状并不相同的时候，我们可以通过扩展数组的方法来实现相加、相减、相乘等操作，这种机制叫做广播（broadcasting）。

比如，一个二维的 ndarray 对象减去列平均值，来对数组的每一列进行取均值化处理：

import numpy as np
# arr为4行3列的ndarray对象
arr = np.random.randn(4,3)
# arr_mean为有3个元素的一维ndarray对象
arr_mean = arr.mean(axis=0)
# 对arr的每一列进行
demeaned = arr - arr_mean
很明显上面代码中的 arr 和 arr_mean 维度并不形同，但是它们可以进行相减操作，这就是通过广播机制来实现的。

广播的原则

广播的原则：如果两个数组的后缘维度（trailing dimension，即从末尾开始算起的维度）的轴长度相符，或其中的一方的长度为1，则认为它们是广播兼容的。广播会在缺失或长度为1的维度上进行，这句话是理解广播的核心。

广播主要发生在两种情况，一种是两个数组的维数不相等，但是它们的后缘维度的轴长相符，另外一种是有一方的长度为1。

我们来看一个例子：

import numpy as np
arr1 = np.array([[0, 0, 0],[1, 1, 1],[2, 2, 2], [3, 3, 3]])
arr2 = np.array([1, 2, 3])
arr_sum = arr1 + arr2
print(arr_sum)
'''
输入结果如下:
[[1 2 3]
 [2 3 4]
 [3 4 5]
 [4 5 6]]
'''
arr1 的 shape 为(4,3)，arr2的 shape 为 (3,)。可以说前者是二维的，而后者是一维的。但是它们的后缘维度相等， arr1 的第二维长度为3 ，和 arr2 的维度相同。

arr1 和 arr2 的 shape 并不一样，但是它们可以执行相加操作，这就是通过广播完成的，在这个例子当中是将 arr2 沿着 0 轴进行扩展。



我们再看一个例子：

import numpy as np
arr1 = np.array([[0, 0, 0],[1, 1, 1],[2, 2, 2], [3, 3, 3]])   #arr1.shape = (4,3)
arr2 = np.array([[1],[2],[3],[4]])    #arr2.shape = (4, 1)
arr_sum = arr1 + arr2
print(arr_sum)
'''
输出结果如下：
[[1 1 1]
 [3 3 3]
 [5 5 5]
 [7 7 7]]
'''
arr1 的 shape 为 (4,3)，arr2 的 shape 为 (4,1)，它们都是二维的，但是第二个数组在1轴上的长度为 1，所以，可以在 1 轴上面进行广播。



编程要求

根据提示，在右侧编辑器 Begin-End 部分补充代码，将输入数据转换为 array 并计算它们的和。

具体要求请参见后续测试样例。
请先仔细阅读右侧上部代码编辑区内给出的代码框架，再开始你的编程工作！

测试说明

平台会对你编写的代码进行测试，对比你输出的数值与实际正确的数值，只有所有数据全部计算正确才能进入下一关。

测试输入：

[[9, 3, 1], [7, 0, 6], [4, 6, 3]] [1, 5, 9] [[9], [6], [7]]

预期输出：

[[19 17 19]
 [14 11 21]
 [12 18 19]]
"""

import numpy as np


def student(a, b, c):
    result = []
    # ********* Begin *********#
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    result = a + b + c
    # ********* End *********#
    return result


if __name__ == '__main__':
    input_data1 = [[9, 3, 1], [7, 0, 6], [4, 6, 3]]
    input_data2 = [1, 5, 9]
    input_data3 = [[9], [6], [7]]
    expected_output = [[19, 17, 19], [14, 11, 21], [12, 18, 19]]
    print(student(input_data1, input_data2, input_data3) == expected_output)
