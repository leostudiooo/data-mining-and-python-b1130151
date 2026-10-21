"""
任务描述

open(name[, mode[, buffering]])函数可以打开诸如txt，csv等格式的文件。
如下，定义了read_file()函数：

def read_file(file):
    \"""接收文件名为参数，读取文件中的数据到字符串中，返回字符串\"""
    with open(file, 'r', encoding='utf-8') as text:  # 创建文件对象
        txt =text.read()      # 读文件为字符串
    return txt     # 返回字符串
read_file(file)可以读取名为file的文件内容，以字符串的形式返回txt，请继续编程统计字符串txt中单词的数量。

提示：统计单词数量时，形如It’s、Let's、don't的缩写形式要按2个单词计数。另外为了处理方便，约定所有测试文件中没有's表示所有格的情况。

输入格式

输入为一行，是一个文本文件名，如example1.txt。

输出格式

输出为一行，是对名为example1.txt的文件内容进行单词数目统计后的结果， 输出共有m个单词，具体格式见示例。

示例

输入：mySunshine.txt
输出：共有7个单词
"""

def read_file(file):
    """接收文件名为参数，读取文件中的数据到字符串中，返回这个字符串"""
    with open(file, 'r', encoding='utf-8') as text:
        txt = text.read()
    return txt

def word_list(txt):
    """接收字符串为参数，用空格替换字符串中所有标点符号，根据空格将字符串切分为列表
    返回值为元素为单词的列表"""
    import re
    txt = re.sub(r"[^\w\s']", ' ', txt)
    words = txt.split()
    return words

def number_of_words(ls):
    """接收一个以单词为元素的列表为参数，返回列表中单词数量，返回值为整型"""
    count = 0
    for word in ls:
        if "'" in word:
            count += 2
        else:
            count += 1
    return count

if __name__ == '__main__':
    filename = input()
    text = read_file('step10/'+filename)
    # testing
    # text = "You're my sunshine, my only sunshine."
    words_list = word_list(text)
    words_counts = number_of_words(words_list)
    print(f'共有{words_counts}个单词')