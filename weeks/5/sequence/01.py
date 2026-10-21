"""任务描述

初始化一个空列表，输入一个正整数 n。
接下来，你将被要求输入 n 个指令，每得到一个指令后，根据指令的字符串进行对应的功能操作。
指令形式及对应功能如下：

insert i e: # 在第 i 个位置插入整数 e。
print:      # 输出列表
remove e:   # 删除第一次出现的整数 e .
append e:   # 在列表的末尾插入整数 e.
sort:       # 按默认规则排序.
pop:        # 弹出列表最后一一个元素
reverse:    # 列表元素逆序.
输入格式
第一行输入一个正整数 n
随后的 n 行，每行输入一个如示例格式的命令（或命令加1或2个整数，要求加入列表的必须是整数）

输出格式
每遇到“print”时，在新的一行输出列表

示例 1
输入：
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
输出：
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

平均代码量 19 行"""

COMMANDS_CAT1 = ["print"]
COMMANDS_CAT2 = ["sort", "pop", "reverse"]
COMMANDS_CAT3 = ["remove", "append"]
COMMANDS_CAT4 = ["insert"]

number_commands = int(input())
operating_list = []

for _ in range(number_commands):
	cmd = input().split()
	if cmd[0] in COMMANDS_CAT1:
		eval(cmd[0] + "(operating_list)")
	elif cmd[0] in COMMANDS_CAT2:
		eval("operating_list." + cmd[0] + "()")
	elif cmd[0] in COMMANDS_CAT3:
		eval("operating_list." + cmd[0] + f"({cmd[1]})")
	elif cmd[0] in COMMANDS_CAT4:
		eval("operating_list." + cmd[0] + f"({cmd[1]}, {cmd[2]})")