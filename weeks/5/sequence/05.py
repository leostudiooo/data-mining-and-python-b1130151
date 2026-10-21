"""
任务描述

输入一系列动物名和其重量，重量单位可能是kg，也可能是t，动物名、与重量间空格分隔，重量数值与单位间无分隔。 按重量由小到大排序以二维列表形式输出。

输入格式
每次输入一个动物名，以及其重量和单位，动物名与重量间用空格分隔，直接输入回车时结束输入(此时输入的字符为空字符串)。

提示：判断输入是否为''空字符串，为True则结束输入。

输出格式
以二维列表形式输出，按重量由小到大升序排序。

示例 1
输入：
北极熊 0.75t
企鹅 35kg
海豹 0.35t
海豚 228kg
白鲸 1.35t

输出：
[['企鹅', '35kg'], ['海豚', '228kg'], ['海豹', '0.35t'], ['北极熊', '0.75t'], ['白鲸', '1.35t']]
"""

animals = []

while True:
	animal_input = input()
	if animal_input == '':
		break
	animals.append(animal_input.split())

# helper function to convert weight to kg for sorting
def weight_to_kg(weight_str):
	if weight_str.endswith('kg'):
		return float(weight_str[:-2])
	elif weight_str.endswith('t'):
		return float(weight_str[:-1]) * 1000
	else:
		raise ValueError("Invalid weight unit")

sorted_animals = sorted(animals, key=lambda x: weight_to_kg(x[1]))
print(sorted_animals)