"""
任务描述

你从武汉搬到美国生活，这里的人都讲英语，你的英语不好，好在你有一个程序，可以把英语译成中文，帮助你与人沟通。
dicts.txt
（注意：词典文件没有精校，存在部分格式不一致的问题，处理时根据空格切分一次，只把英文和中文解释切分开。）

输入

输入一个英文句子

输出

输出英文句子中每个单词的中文意思，每行一个单词，单词字母转小写，"'s" 用 " is"替换，"n't" 用" not" 替换（替换为空格加is或not），单词与意义间用空格分隔，当查询的词在文件中不存在时，输出'自己猜'

示例 1

输入：
For others, but to live for yourself.
输出：
for 给，作...用的
others 自己猜
but 但是，除了
to 向，到
live 居住,生存 活的
for 给，作...用的
yourself 你(们)自己
"""

dicts = {}
# with open('step15/dicts.txt', 'r', encoding='utf-8') as data:
with open ('dicts.txt', 'r', encoding='utf-8') as data:
    for x in data:
        word,trans = x.strip().split(maxsplit=1)
        dicts[word]=trans

sentence = input().strip().lower()
sentence = sentence.replace("'s", " is").replace("n't", " not")
import re
sentence = re.sub(r'[^\w\s]', '', sentence)

words = sentence.split()

for word in words:
    print(f"{word} {dicts.get(word, '自己猜')}")