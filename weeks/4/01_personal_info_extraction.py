"""
任务描述

用户输入自己的个人信息，格式如下：
0122923450321 王昊 法学1801 河北 2001年

数据分别表示：学号 姓名 专业班级 籍贯 出生年份，各数据间空格间隔.
有些用户没有按照规则输入数据，输入自己出生年份的时候写成了类似‘1900年生’或‘出生于1985’或‘19岁生于2006年11月20日’的数据格式。请注意程序此时仍然需要正确读取该项数据，本题保证这些用户输入时一定只含有1个4位数字连续组成的年份数据。

请按照输出样式输出姓名，班级，出生年份。

提示：

列表中的数据和字符串当中的字符一样，都具有有序的索引，且引用数据和切片方式一致。
str.isdigit()可以帮助判断字符串是否全部由数字字符组成，返回值为'True'或'False'

输入格式
按如下示例，在一行内依次输入5个字符串，分别表示：学号 姓名 专业班级 籍贯 出生年份，各数据间空格间隔
0122923450321 王昊 法学1801 河北 2001年

输出格式
按如下示例，分行依次输出姓名，班级，出生年份

姓名：王昊
班级：法学1801
出生：2001年

示例
输入：
0122923450321 王昊 法学1801 河北 2001年

输出：    
姓名：王昊
班级：法学1801
出生：2001年
"""

YEAR_STRING_WINDOW = 4

#input
split_content = input().split(" ")

# detect continuous 4 digit number in the last content
last_content = split_content[-1]
for i in range(len(last_content) - YEAR_STRING_WINDOW + 1):
	if last_content[i:i + YEAR_STRING_WINDOW].isdigit():
		split_content[-1] = last_content[i:i + YEAR_STRING_WINDOW]
		break
split_content[-1] = split_content[-1] + "年"

# output
print("姓名：" + split_content[1])
print("班级：" + split_content[2])
print("出生：" + split_content[-1])