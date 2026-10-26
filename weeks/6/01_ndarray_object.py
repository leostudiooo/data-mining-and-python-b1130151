"""
编程要求

根据提示，在右侧编辑器Begin-End中填充代码，根据测试用例的输入，实例化出对应的ndarray对象并打印。

具体要求请参见后续测试样例。
请先仔细阅读右侧上部代码编辑区内给出的代码框架，再开始你的编程工作！

测试说明

平台会对你编写的代码进行测试，对比你输出的数值与实际正确的数值，只有所有数据全部计算正确才能进入下一关。

shape：为需要实例化出来的ndarray对象的shape；

data：表示需要实例化出来的ndarray对象中元素的值。

例如：{'shape':[1, 2], 'data':[[1, 2]]}表示ndarray对象的形状为1行2列，第1行第1列的值为1，第1行第2列的值为2。

测试输入：
{'shape':[1, 2], 'data':[[1, 2]]}

预期输出：
[[1 2]]
"""

import numpy as np

def print_ndarray(input_data):
    '''
    实例化ndarray对象并打印
    :param input_data: 测试用例，类型为字典类型
    :return: None
    '''

    #********* Begin *********#
    arr = np.array(input_data['data']).reshape(input_data['shape'])
    print(arr)
    #********* End *********#
    
if __name__ == '__main__':
	input_data = eval(input())
	print_ndarray(input_data)