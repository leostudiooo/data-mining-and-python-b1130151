"""

相关知识

为了完成本关任务，你需要掌握：怎样改变ndarray对象的形状。

怎样改变ndarray对象的形状

改变形状

上一关介绍了怎样实例化ndarray对象，比如想实例化一个3行4列的二维数组，并且数组中的值全为0。就可能会写如下代码：

import numpy as np
a = np.zeros((3, 4))
那如果想把a变成4行3列的二维数组，怎么办呢？比较聪明的同学可能会想到这样的代码：

import numpy as np
a = np.zeros((3, 4))
# 直接修改shape属性
a.shape = [4, 3]
最后你会发现，这样的代码可以完成功能，但是这种直接改属性的方式太粗暴了，不符合良好的编程规范。

更加优雅的解决方式是使用NumPy为我们提供了一个用来改变ndarray对象的shape的函数，叫 reshape 。

NumPy为了照顾偏向于面向对象或者这偏向于面向过程这两种不同风格的程序员，提供了2种调用 reshape 函数的方式(其实很多函数都提供了两种风格的接口)。

如果你更偏向于面向对象，那么你可以想象成ndarray对象中提供好了一个叫reshape成员函数。代码如下:

import numpy as np
a = np.zeros((3, 4))
# 调用a的成员函数reshape将3行4列改成4行3列
a = a.reshape((4, 3))
如果你更偏向于面向过程，NumPy在它的作用域内实现了reshape函数。代码如下：

import numpy as np
a = np.zeros((3, 4))
# 调用reshape函数将a变形成4行3列
a = np.reshape(a, (4, 3))
PS:不管是哪种方式的reshape，都不会改变原ndarray的形状，而是将源ndarray进行深拷贝并进行变形操作，最后再将变形后的数组返回出去。也就是说如果代码是np.reshape(a, (4, 3))那么a的形状不会被修改！

如果想优雅的直接改变源ndarray的形状，可以使用resize函数。代码如下：

import numpy as np
a = np.zeros((3, 4))
# 将a从3行4列的二维数组变成一个有12个元素的一维数组
a.resize(12)
小技巧

有的时候懒得去算每个维度上的长度是多少，比如现在有一个6行8列的ndarray，然后想把它变形成有2列的ndarray(行的数量我懒得去想)，此时我们可以在行的维度上传个-1即可，代码如下：

import numpy as np
a = np.zeros((6, 8))
# 行的维度上填-1，会让numpy自己去推算出行的数量，很明显，行的数量应该是24
a = a.reshape((-1, 2))
也就是说在变形操作时，如果某个维度上的值为-1，那么该维度上的值会根据其他维度上的值自动推算。

PS：-1虽好，可不能贪杯！如果代码改成a = a.reshape((-1, -1))，NumPy会认为你是在刁难他，并向你抛出异常ValueError: can only specify one unknown dimension。

编程要求

根据提示，在右侧编辑器Begin-End中填充代码，根据测试用例的输入，将列表转换成ndarray后变形成一维数组并将其打印。

具体要求请参见后续测试样例。
请先仔细阅读右侧上部代码编辑区内给出的代码框架，再开始你的编程工作！

测试说明

平台会对你编写的代码进行测试，对比你输出的数值与实际正确的数值，只有所有数据全部计算正确才能进入下一关。

测试输入：
[[1, 2, 3], [4, 5, 6]]
预期输出：
[1, 2, 3, 4, 5, 6]

import numpy as np
a = np.zeros((3, 4))
``````python
import numpy as np
a = np.zeros((3, 4))
``````python
import numpy as np
a = np.zeros((3, 4))
"""

import numpy as np


def reshape_ndarray(input_data):
    '''
    将ipnut_data转换成ndarray后将其变形成一位数组并打印
    :param input_data: 测试用例，类型为list
    :return: None
    '''

    #********* Begin *********#
    arr = np.array(input_data).reshape(-1)
    print(arr)
    #********* End *********#
    
if __name__ == '__main__':
	input_data = eval(input())
	reshape_ndarray(input_data)