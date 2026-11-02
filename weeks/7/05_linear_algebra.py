"""
任务描述

本关任务：编写一个能求解线性方程的函数。

相关知识

为了完成本关任务，你需要掌握：

numpy 的线性代数；
常用函数。
numpy 的线性代数

线性代数（如矩阵乘法、矩阵分解、行列式以及其他方阵数学等）是任何数组库的重要组成部分，一般我们使用*对两个二维数组相乘得到的是一个元素级的积，而不是一个矩阵点积。因此 numpy 提供了线性代数函数库 linalg ，该库包含了线性代数所需的所有功能。

常用的 numpy.linalg 函数：

函数	说明
dot	矩阵乘法
vdot	两个向量的点积
det	计算矩阵的行列式
inv	计算方阵的逆
svd	计算奇异值分解（SVD）
solve	解线性方程组 Ax=b，A是一个方阵
matmul	两个数组的矩阵积
常用函数

dot()：该函数返回俩个数组的点积。对于二维向量，效果等于矩阵乘法；对于一维数组，它是向量的内积；对于N维数组，它是a的最后一个轴上的和与b的倒数第二个轴的乘积。

a=np.array([[1,2],[3,4]])
a1=np.array([[5,6],[7,8]])
np.dot(a,a1)
'''
输出：array([[19, 22],
       [43, 50]])
'''
det()：该函数用于计算输入矩阵的行列式。

a = np.array([[14, 1], [6, 2]])
a=linalg.det(a)
print(a)
'''
输出：21.999999999999996
'''
inv()：该函数用于计算方阵的逆矩阵。逆矩阵的定义维如果两个方阵 A、B，使得 AB = BA = E，则A称为可逆矩阵，B 为 A 的逆矩阵，E 为单位矩阵。

 a=np.array([[1,2],[3,4]])
 b=linalg.inv(a)
 print(np.dot(a,b))
'''
输出：array([[1.0000000e+00, 0.0000000e+00],
       [8.8817842e-16, 1.0000000e+00]])
'''
solve()：该函数用于计算线性方程的解。

假设有如下方程组：3x+2y=7  x+4y=14；

写成矩阵的形式：[[3,2][1,4]]*[[x],[y]]=[[7],[14]]；

解如上方程组代码如下：

 a=np.array([[3,2], [1,4]])
 b=np.array([[7],[14]])
 linalg.solve(a,b)
'''
 输出:array([[0. ],
       [3.5]])
 最后解出x=0，y=3.5
'''
matmul()：函数返回两个数组的矩阵乘积。如果参数中有一维数组，则通过在其维度上附加1来提升为矩阵，并在乘法之后去除。

a=[[3,4],[5,6]]
b=[[7,8],[9,10]]
np.matmul(a,b)
'''
输出：array([[ 57,  64],
       [ 89, 100]])
'''
b=[7,8]
np.matmul(a,b)
'''
输出：array([53, 83])
'''
svd()：奇异值分解是一种矩阵分解的方法，该函数用来求解 SVD。

a=[[0,1],[1,1],[1,0]]
linalg.svd(a)
'''
输出:(array([[-4.08248290e-01,  7.07106781e-01,  5.77350269e-01],
       [-8.16496581e-01,  2.64811510e-17, -5.77350269e-01],
       [-4.08248290e-01, -7.07106781e-01,  5.77350269e-01]]), array([1.73205081, 1.        ]), array([[-0.70710678, -0.70710678],
       [-0.70710678,  0.70710678]]))
'''
编程要求

根据提示，在右侧编辑器 Begin-End 部分补充代码，计算性别为男的线性方程解，前两个数为方程左边，最后一个数为方程右边。

具体要求请参见后续测试样例。
请先仔细阅读右侧上部代码编辑区内给出的代码框架，再开始你的编程工作！

测试说明

平台会对你编写的代码进行测试，对比你输出的数值与实际正确的数值，只有所有数据全部计算正确才能进入下一关。

测试输入：

[["男",2,4,40],["女",8,3,17],["男",8,6,24]]

预期输出：

[[-7.2]
 [13.6]]
提示：测试数据的方程为 2x+4y=40，8x+6y=24。
"""

from numpy import linalg
import numpy as np


def student(input_data):
    '''
    将输入数据筛选性别为男，再进行线性方程求解
    :param input_data:类型为`list`的输入数据
    :return:类型为`ndarray`，无男生数据时返回空列表[]
    '''
    result = []

    # ********* Begin *********#
    male_rows = []

    for row in input_data or []:
        try:
            if row is None or len(row) < 4:
                continue

            gender = str(row[0]).strip()
            if gender != '男':
                continue

            x1 = float(row[1])
            x2 = float(row[2])
            y = float(row[3])

            male_rows.append([x1, x2, y])
        except (TypeError, ValueError, IndexError):
            continue

    # 防御：没有男生，或男生不足 2 行，无法构造 2x2 方程，返回空列表
    if len(male_rows) < 2:
        return []

    use_rows = male_rows[:2]
    A = np.asarray([[r[0], r[1]] for r in use_rows], dtype=float)
    b = np.asarray([r[2] for r in use_rows], dtype=float)

    try:
        result = linalg.solve(A, b)
    except linalg.LinAlgError:
        result, *_ = linalg.lstsq(A, b, rcond=None)

    result = np.asarray(result, dtype=float).reshape(-1, 1)

    if result.size and not np.all(np.isfinite(result)):
        result, *_ = linalg.lstsq(A, b, rcond=None)
        result = np.asarray(result, dtype=float).reshape(-1, 1)

    # ********* End *********#
    return result


if __name__ == '__main__':
    # 正常情况
    print(student([["男", 2, 4, 40], ["女", 8, 3, 17], ["男", 8, 6, 24]]))
    # 只有女生
    print(student([["女", 8, 3, 17]]))
