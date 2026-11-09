"""
相关知识

为了完成本关任务，你需要掌握：算术运算（+，-，*，/）。

算术运算（+，-，*，/）

DataFrame 中的算术运算是 df 中对应位置的元素的算术运算，如果没有共同的元素，则用 NaN 代替。

In[5]: df1 = DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
In[6]: df2 = DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))
In[9]: df1+df2
Out[9]: 
    a   b   c   d   e
0   0   2   4   6 NaN
1   9  11  13  15 NaN
2  18  20  22  24 NaN
3 NaN NaN NaN NaN NaN
此外，如果我们想设置默认的其他填充值，而非 NaN 的话，可以传入填充值。

In[11]: df1.add(df2, fill_value=0)
Out[11]: 
    a   b   c   d   e
0   0   2   4   6   4
1   9  11  13  15   9
2  18  20  22  24  14
3  15  16  17  18  19
编程要求

根据提示，在右侧编辑器 Begin-End 内补充代码：

让 df1 与 df2 相加得到 df3，并设置默认填充值为 4。
测试说明

如果答案正确，则会输出 True。
"""

# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import numpy as np
import pandas as pd


def add_way():
    '''
    返回值:
    df3: 一个DataFrame类型数据
    '''

    # df1,df2是DataFrame类型数据
    df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
    df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    df3 = df1.add(df2, fill_value=4)
    # ********** End **********#

    # 返回df3
    return df3
