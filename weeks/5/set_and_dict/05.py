"""
任务描述

将用户输入用逗号分隔的一系列人名做为键，用户输入的逗号分隔的手机号做为值，创建字典MyDict，输入一个正整数 n，你将被要求读入 n 个输入（输入形式如下所示），每得到一个输入后，根据输入进行操作。

add name number:      # 在字典中加入以name为键、以number为值的元素
print:                # 输出字典
del name:             # 删除字典中以name为键的元素，当name不存在时，输出'键不存在'
update name number:   # 更新字典中以name为键的元素的值为number
value:                # 以列表形式输出字典中的所有值
key:                  # 以列表形式输出字典中所有键
clear:                # 清空字典
输入

第一行输入一个正整数 n
第二行输入用逗号分隔的多个人名
第三行输入的逗号分隔的、与第二行相同数量的手机号
随后的 n 行，每行输入一个如示例格式的命令，命令与参数间空格分隔

输出

每遇到“print”时，在新的一行输出字典 

示例 1

输入:
8
Tom,Jack,Lee
13988776655,13855664488,13644668888
key
value
print
clear
add ethan 17700001111
add Tom 13988776655
update Tom 13000112222
print
输出:
['Tom', 'Jack', 'Lee']
['13988776655', '13855664488', '13644668888']
{'Tom': '13988776655', 'Jack': '13855664488', 'Lee': '13644668888'}
{'ethan': '17700001111', 'Tom': '13000112222'}
"""

n = int(input().strip())

names = input().strip().split(',')
phones = input().strip().split(',')

MyDict = dict(zip(names, phones))

for _ in range(n):
    command = input().strip().split()
    op = command[0]

    if op == 'add':
        name, number = command[1], command[2]
        MyDict[name] = number
    elif op == 'print':
        print(MyDict)
    elif op == 'del':
        name = command[1]
        if name in MyDict:
            del MyDict[name]
        else:
            print('键不存在')
    elif op == 'update':
        name, number = command[1], command[2]
        MyDict[name] = number
    elif op == 'value':
        print(list(MyDict.values()))
    elif op == 'key':
        print(list(MyDict.keys()))
    elif op == 'clear':
        MyDict.clear()