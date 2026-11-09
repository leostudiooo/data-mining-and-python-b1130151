"""
相关知识

为了完成本关任务，你需要掌握：

读取 CSV；
查看前 n 行；
查看后 n 行；
查看总行数；
修改列名。
在使用机器学习工具包对数据进行修改、探索和分析之前，我们必须先讲外部数据导入。使用 Pandas 导入数据比 Numpy 要容易。在这里我们将使用英国降雨数据，数据已下好并放在本实训的当前文件夹。

读取 CSV

# Reading a csv into Pandas.
# 如果数据集中有中文的话，最好在里面加上 encoding = 'gbk' ，以避免乱码问题。后面的导出数据的时候也一样。
df = pd.read_csv('uk_rain_2014.csv', header=0)
这里我们从 csv 文件里导入了数据，并储存在 DataFrame 中。这一步非常简单，你只需要调用 read_csv 然后将文件的路径传进去就行了。header 关键字告诉 Pandas 哪些是数据的列名。如果没有列名的话就将它设定为 None。
数据导入 pandas 之后，我们该怎么查看数据呢？

查看前 n 行

# Getting first x rows.
df.head(5)
查看后 n 行

# Getting last x rows.
df.tail(5)
查看总行数

# Finding out how many rows dataset has.
len(df)
修改列名

我们通常使用列的名字来在 Pandas 中查找列。这一点很好而且易于使用，但是有时列名太长，我们需要缩短列名。

    # Changing column labels.
    df.columns = ['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']
编程要求

根据提示，在右侧编辑器 Begin-End 内补充代码：

将 test3/uk_rain_2014.csv 中的数据导入到 df1 中；

将列名修改为 ['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']；

计算 df1 的总行数并存储在 length1 中。

测试说明

如果答案正确，则会输出 True。
"""

# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd


def read_csv_data(file_path="test3/uk_rain_2014.csv"):
    '''
    返回值:
    df1: 一个DataFrame类型数据
    length1: 一个int类型数据
    '''

    df1 = pd.read_csv(file_path, header=0)
    df1.columns = ['water_year', 'rain_octsep', 'outflow_octsep',
                   'rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']
    length1 = len(df1)

    # 返回df1,length1
    return df1, length1


if __name__ == '__main__':
    print(read_csv_data("/Users/lilingfeng/Repositories/data-mining-and-python-b1130151/weeks/8/uk_rain_2014.csv"))
