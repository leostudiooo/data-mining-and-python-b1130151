"""
任务描述

第一行输入一个正整数 N，随后的N 行各输入一个人的姓名和年龄，中间用空格分隔（形如 “Tom 18” ），将字符串转为形如 {"name":"Tom","age":18} 的字典，按顺序加入到列表中，得到一个元素为字典的列表，分别根据年龄和姓名对其排序输出。

输入格式

第一行输入一个正整数 N
随后的N 行各输入一个形如 “Tom  18” 的字符串

输出格式

根据年龄排序的列表
根据姓名排序的列表

示例 1

输入:
4
Tom 18
Jerry 47
Cat 20
Doge 33
输出:
[{'name': 'Tom', 'age': 18}, {'name': 'Cat', 'age': 20}, {'name': 'Doge', 'age': 33}, {'name': 'Jerry', 'age': 47}]
[{'name': 'Cat', 'age': 20}, {'name': 'Doge', 'age': 33}, {'name': 'Jerry', 'age': 47}, {'name': 'Tom', 'age': 18}]
"""

number_lines = int(input())
people_list = []
for _ in range(number_lines):
	name, age = input().split()
	person_dict = {"name": name, "age": int(age)}
	people_list.append(person_dict)

print(sorted(people_list, key=lambda x: x["age"]))
print(sorted(people_list, key=lambda x: x["name"]))