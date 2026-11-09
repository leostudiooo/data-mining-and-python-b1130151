"""
相关知识

为了完成本关任务，你需要掌握：

层次化索引；
索引方式；
内层选取；
数据重塑。
层次化索引

层次化索引(hierarchical indexing)是 pandas 的一项重要功能，它使我们能在一个轴上拥有多个（两个以上）索引级别。请看以下例子：

In[1]:data = Series(np.random.randn(10), index = [['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd' ],[1,2,3,1,2,3,1,2,2,3]])
In[2]:data
Out[2]:
a  1    0.169239
   2    0.689271
   3    0.879309
b  1   -0.699176
   2    0.260446
   3   -0.321751
c  1    0.893105
   2    0.757505
d  2   -1.223344
   3   -0.802812
dtype: float64
索引方式

In[3]:data['b':'d']
Out[3]:
b  1   -0.699176
   2    0.260446
   3   -0.321751
c  1    0.893105
   2    0.757505
d  2   -1.223344
   3   -0.802812
dtype: float64
内层选取

In[4]:data[:, 2]
Out[4]:
a    0.689271
b    0.260446
c    0.757505
d   -1.223344
dtype: float64
数据重塑

将 Series 转化成 DataFrame:

in[5]:data.unstack()
Out[5]:
1                    2            3
a    0.169239    0.689271    0.879309
b    -0.699176   0.260446  -0.321751
c    0.893105    0.757505    NaN
d    NaN        -1.223344   -0.802812
编程要求

根据提示，在右侧编辑器 Begin-End 内补充代码:

对 s1 进行数据重塑，转化成 DataFrame 类型，并复制到 d1。
测试说明

编写代码之后，点击测评即可。
"""

# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd
import numpy as np


def suoying():
    '''
    返回值:
    d1: 一个DataFrame类型数据
    '''
    # s1是Series类型数据
    s1 = Series(np.random.randn(10), index=[
                ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    d1 = s1.unstack()
    # ********** End **********#

    # 返回d1
    return d1


suoying()
