"""
相关知识

为了完成本关任务，你需要掌握：删除指定轴上的项。

删除指定轴上的项

即删除 Series 的元素或 DataFrame 的某一行（列）的意思，我们可以通过对象的 drop(labels, axis=0) 方法实现此功能。

删除 Series 的一个元素：

In[11]: ser = Series([4.5,7.2,-5.3,3.6], index=['d','b','a','c'])
In[13]: ser.drop('c')
Out[13]: 
d    4.5
b    7.2
a   -5.3
dtype: float64
删除 DataFrame 的行或列：

In[17]: df = DataFrame(np.arange(9).reshape(3,3), index=['a','c','d'], columns=['oh','te','ca'])
In[18]: df
Out[18]: 
   oh  te  ca
a   0   1   2
c   3   4   5
d   6   7   8
In[19]: df.drop('a')
Out[19]: 
   oh  te  ca
c   3   4   5
d   6   7   8
In[20]: df.drop(['oh','te'],axis=1)
Out[20]: 
   ca
a   2
c   5
d   8
需要注意的是 drop() 返回的是一个新对象，原对象不会被改变。

编程要求

根据提示，在右侧编辑器 Begin-End 内补充代码：

在 s1 中删除 z 行，并赋值到 s2；

d1 中删除 yy 列，并赋值到 d2。

测试说明

如果答案正确，则会输出 True。
"""

# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import numpy as np
import pandas as pd


def delete_data():
    '''
    返回值:
    s2: 一个Series类型数据
    d2: 一个DataFrame类型数据
    '''

    # s1是Series类型数据，d1是DataFrame类型数据
    s1 = Series([5, 2, 4, 1], index=['v', 'x', 'y', 'z'])
    d1 = DataFrame(np.arange(9).reshape(3, 3), columns=['xx', 'yy', 'zz'])
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    s2 = s1.drop('z')
    d2 = d1.drop('yy', axis=1)
    # ********** End **********#

    # 返回s2,d2
    return s2, d2
