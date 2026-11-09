"""
任务描述

本关任务：根据编程要求，完成相关代码的编写。

相关知识

为了完成本关任务，你需要掌握：

DataFrame 创建；
修改行名；
添加修改；
添加 Series 类型；
添加新列。
DataFrame 是一个表格型的数据结构，是以一个或多个二维块存放的数据表格（层次化索引），DataFrame 既有行索引还有列索引，它有一组有序的列，每列既可以是不同类型（数值、字符串、布尔型）的数据，或者可以看做由 Series 组成的字典。

DataFrame 创建

    dictionary = {'state':['0hio','0hio','0hio','Nevada','Nevada'],
             'year':[2000,2001,2002,2001,2002],
             'pop':[1.5,1.7,3.6,2.4,2.9]}
    frame = DataFrame(dictionary)
修改行名

    frame=DataFrame(dictionary,index=['one','two','three','four','five'])
添加修改

    frame['add']=[0,0,0,0,0]
添加 Series 类型

    value = Series([1,3,1,4,6,8],index = [0,1,2,3,4,5])
    frame['add1'] = value
添加新列

    1、直接在后面新增一列
    指明列名，并赋值即可：
    data[‘列名’]=[1,2]
    2、在指定位置新增一列
    用insert()函数，data.insert(位置,列名,列值)，例如：
    data.insert(2,‘c’,’’)
编程要求

根据提示，在右侧编辑器 Begin-End 内补充代码：

创建一个五行三列的名为 df1 的 DataFrame 数组，列名为 [states,years,pops]，行名 ['one','two','three','four','five']；

给 df1 添加新列，列名为 new_add，值为 [7,4,5,8,2]。

测试说明

如果答案正确，则会输出 True。
"""

# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd


def create_dataframe():
    '''
    返回值:
    df1: 一个DataFrame类型数据
    '''

    df1 = DataFrame(columns=['states', 'years', 'pops'], index=['one', 'two', 'three', 'four', 'five'])
    df1.insert(3, 'new_add', [7, 4, 5, 8, 2])
    return df1

if __name__ == '__main__':
	df1 = create_dataframe()
	print(df1)