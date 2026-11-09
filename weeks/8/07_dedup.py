"""
相关知识

为了完成本关任务，你需要掌握：

duplicated()；
drop_duplicates()。
duplicated()

DataFrame 的 duplicated 方法返回一个布尔型 Series，表示各行是否是重复行。具体用法如下：

In[1]: df = DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[1,1,2,3,3,4,4]})
In[2]: df
Out[2]: 
    k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
In[3]: df.duplicated()
Out[3]: 
0    False
1     True
2    False
3    False
4     True
5    False
6     True
dtype: bool
drop_duplicates()

drop_duplicates() 用于去除重复的行数，具体用法如下：

In[4]: df.drop_duplicates()
Out[4]: 
    k1  k2
0  one   1
2  one   2
3  two   3
5  two   4
编程要求

根据提示，在右侧编辑器 Begin-End 内补充代码:

去除 df1 中重复的行，并把结果保存到 df2 中。
测试说明

如果答案正确，则会输出 True。
"""

# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd


def delete_duplicated():
    '''
    返回值:
    df2: 一个DataFrame类型数据
    '''

    # df1是DataFrame类型数据
    df1 = DataFrame({'k1': ['one'] * 3 + ['two'] *
                    4, 'k2': [1, 1, 2, 3, 3, 4, 4]})
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    df2 = df1.drop_duplicates()
    # ********** End **********#

    # 返回df2
    return df2
