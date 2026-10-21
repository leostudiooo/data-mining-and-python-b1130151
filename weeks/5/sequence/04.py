"""
任务描述

有以下两个二维列表。
第一个列表的元素是元组，请对其按列表元素的第 2 个元素值从小到大进行排序输出，输出其前 m 项；列表一： 
[('dungeon',7),('winterfell',4),('bran',9),('meelo',6)]
第二个列表的元素仍是列表，请对其分别按每个元素的第 1 和第 3 个元素值从小到大进行排序，输出其前 n 项。列表二： [[ 'Angle', '0121701100106',99], [ 'Jack', '0121701100107',86], [ 'Tom', '0121701100109',65], [ 'Smith', '0121701100111', 100], ['Bob', '0121701100115',77], ['Lily', '0121701100117', 59]]

m 和 n 是由用户输入的非负整数，当 m 或 n 大于列表长度时，对整个列表进行排序输出。
输入格式
在两行中分别输入正整数m 和 n

输出格式
列表一排序后的前 m 项
列表二按第 1 个元素值升序排序的前 n 项
列表二按第 3 个元素值升序排序的前 n 项

示例
输入：
2
3

输出：
[('winterfell', 4), ('meelo', 6)]
[['Angle', '0121701100106', 99], ['Bob', '0121701100115', 77], ['Jack', '0121701100107', 86]]
[['Lily', '0121701100117', 59], ['Tom', '0121701100109', 65], ['Bob', '0121701100115', 77]]

平均代码量 12 行
"""
LIST_1 = [('dungeon', 7), ('winterfell', 4), ('bran', 9), ('meelo', 6)]
LIST_2 = [['Angle', '0121701100106', 99], ['Jack', '0121701100107', 86], ['Tom', '0121701100109', 65], [
    'Smith', '0121701100111', 100], ['Bob', '0121701100115', 77], ['Lily', '0121701100117', 59]]

number_m = int(input())
number_n = int(input())

sorted_list_1 = sorted(LIST_1, key=lambda x: x[1])
sorted_list_2_by_first = sorted(LIST_2, key=lambda x: x[0])
sorted_list_2_by_third = sorted(LIST_2, key=lambda x: x[2])

print(sorted_list_1[:number_m])
print(sorted_list_2_by_first[:number_n])
print(sorted_list_2_by_third[:number_n])