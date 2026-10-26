"""
相关知识

为了完成本关任务，你需要掌握：

简单随机数生成；

概率分布随机数生成；

随机种子。

简单随机数生成

NumPy的random模块下提供了许多生成随机数的函数，如果对于随机数的概率分布没有什么要求，则通常可以使用random_sample、choice、randint等函数来实现生成随机数的功能。

random_sample

random_sample用于生成区间为[0, 1]的随机数，需要填写的参数size表示生成的随机数的形状，比如size=[2, 3]那么则会生成一个2行3列的ndarray，并用随机值填充。示例代码如下：

import numpy as np
'''
结果可能为[[0.32343809, 0.38736262, 0.42413616]
          [0.86190206, 0.27183736, 0.12824812]]
'''
print(np.random.random_sample(size=[2, 3]))
choice

如果想模拟像掷骰子、扔硬币等这种随机值是离散值，而且知道范围的可以使用choice实现。choice的主要参数是a、size和replace。a是个一维数组，代表你想从a中随机挑选；size是随机数生成后的形状。假如模拟5次掷骰子，replace用来设置是否可以取相同元素，True表示可以取相同数字；False表示不可以取相同数字，默认是True，代码如下：

import numpy as np
'''
掷骰子时可能出现的点数为1, 2, 3, 4, 5, 6，所以a=[1,2,3,4,5,6]
模拟5此掷骰子所以size=5
结果可能为 [1 4 2 3 6]
'''
print(np.random.choice(a=[1, 2, 3, 4, 5, 6], size=5,replace=False))
randint

randint的功能和choice差不多，只不过randint只能生成整数，而choice生成的数与a有关，如果a中有浮点数，那么choice会有概率挑选到浮点数。

randint的参数有3个，分别为low，high和size。其中low表示随机数生成时能够生成的最小值，high表示随机数生成时能够生成的最大值减1。也就是说randint生成的随机数的区间为[low, high)。假如模拟5次掷骰子，代码如下：

import numpy as np
'''
掷骰子时可能出现的点数为1, 2, 3, 4, 5, 6，所以low=1,high=7
模拟5此掷骰子所以size=5
结果可能为 [6, 4, 3, 1, 3]
'''
print(np.random.randint(low=1, high=7, size=5)
概率分布随机数生成

如果对于产生的随机数的概率分布有特别要求，NumPy同样提供了从指定的概率分布中采样得到的随机值的接口。在这里主要介绍高斯分布。

高斯分布又称为正态分布，其分布图形如下：




上图中横轴为随机变量的值（在这里可以看成是产生的随机值），纵轴表示随机变量对应的概率（在这里可以看成是随机值被挑选到的概率）。

其实在日常生活中有很多现象或多或少都符合高斯分布。比如某个地方的高考分数，一般来说高考分数非常低和高考分数非常高的学生都比较少，而分数中规中矩的学生比较多，如果所统计的数据足够大，那么高考分数的概率分布也会和上图一样，中间高，两边低。

想要实现根据高斯分布来产生随机值，可以使用normal函数。示例代码如下：

import numpy as np
'''
根据高斯分布生成5个随机数
结果可能为：[1.2315868, 0.45479902, 0.24923969, 0.42976352, -0.68786445]
从结果可以看出0.4左右得值出现的次数比较高，1和-0.7左右的值出现的次数比较低。
'''
print(np.random.normal(size=5)
其中normal函数除了size参数外，还有两个比较重要的参数就是loc和scale，它们分别代表高斯分布的均值和方差。loc影响的分布中概率最高的点的位置，假设loc=2，那么分布中概率最高的点的位置就是2。下图体现了loc对分布的影响，其中蓝色f分布的loc=0，红色分布的loc=5。




scale影响的是分布图形的胖瘦，scale越小，分布就越又高又瘦，scale越大，分布就越又矮又胖。下图体现了scale对分布的影响，其中蓝色分布的scale=0.5，红色分布的scale=1.0。




所以，想要根据均值为1，方差为10的高斯分布来生成5个随机值，代码如下：

import numpy as np
print(np.random.normal(loc=1, scale=10, size=5)
随机种子

前面说了这么多随机数生成的方法，那么随机数是怎样生成的呢？其实计算机产生的随机数是由随机种子根据一定的计算方法计算出来的数值。所以只要计算方法固定，随机种子固定，那么产生的随机数就不会变！

如果想要让每次生成的随机数不变，那么就需要设置随机种子（随机种子其实就是一个0到2 
32
 −1的整数）。设置随机种子很长简单，调用seed函数并设置随机种子即可，代码如下：

import numpy as np
# 设置随机种子为233
np.random.seed(seed=233)
data = [1, 2, 3, 4]
# 随机从data中挑选数字，结果为4
print(np.random.choice(data))
# 随机从data中挑选数字，结果为4
print(np.random.choice(data))
编程要求

根据提示，在右侧编辑器Begin-End处补充代码，将测试用例输入打乱顺序并返回打乱结果。

具体要求请参见后续测试样例。
注意：评测程序内部已经设置好了随机种子，为了顺利评测，请使用np.random.choice()函数来实现打乱顺序。

请先仔细阅读右侧上部代码编辑区内给出的代码框架，再开始你的编程工作！

测试说明

平台会对你编写的代码进行测试，对比你输出的数值与实际正确的数值，只有所有数据全部计算正确才能进入下一关。

测试输入：
[1, 2, 3, 4, 5, 6]
预期输出：
[4, 3, 5, 1, 2, 6]
"""

import numpy as np


def shuffle(input_data):
    '''
    打乱input_data并返回打乱结果
    :param input_data: 测试用例输入，类型为list
    :return: result，类型为list
    '''

    # 保存打乱的结果
    result = []
    #********* Begin *********#
    result = np.random.choice(input_data, size=len(input_data), replace=False).tolist()
    #********* End *********#
    return result

if __name__ == '__main__':
	input_data = eval(input())
	print(shuffle(input_data))