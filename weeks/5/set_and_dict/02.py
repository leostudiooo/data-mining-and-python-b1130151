"""
任务描述

sale2018.csv
sale2019.csv
文件中包含有2018和2019手机销售榜单数据（市场份额百分数），请根据要求升序输出分析结果：

1.输入'1'时，以列表形式在两行中分别输出2019年和2018年上榜品牌
2.输入'2'时，以列表形式输出2019年和2018年都上榜的品牌
3.输入'3'时，以列表形式输出2019年和2018年上榜的所有品牌
4.输入'4'时，以列表形式输出2019年新上榜品牌
5.输入'5'时，以列表形式输出2019年新上榜和落榜品牌

读取文件可参考代码：

with open('sale2019.csv', 'r', encoding='utf-8') as data2019: 
    sale2019 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in data2019]
示例

输入：
5

输出：
['中兴', '联想', '金立']
"""

SALES2018_CSV_CONTENT = """华为,30.5
vivo,19.1
OPPO,19.5
小米,12.3
Apple,13.5
魅族,2.4
三星,1.5
金立,1.2"""

SALES2019_CSV_CONTENT = """华为,34.3
vivo,18.5
OPPO,18.6
小米,12.3
Apple,8.6
魅族,1.8
三星,1.5
联想,0.8
中兴,0.6"""

sale2019 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in SALES2019_CSV_CONTENT.splitlines()]
sale2018 = [[line.strip().split(',')[0], float(line.strip().split(',')[1])] for line in SALES2018_CSV_CONTENT.splitlines()]

# with open('step7/sale2019.csv','r',encoding='utf-8') as data2019:
#     sale2019 = [[line.strip().split(',')[0],float(line.strip().split(',')[1])] for line in data2019]
# with open('step7/sale2018.csv','r',encoding='utf-8') as data2018:
#     sale2018 = [[line.strip().split(',')[0],float(line.strip().split(',')[1])] for line in data2018]

selection = input()

if selection == '1':
	brands_2019 = sorted([item[0] for item in sale2019])
	brands_2018 = sorted([item[0] for item in sale2018])
	print(brands_2019)
	print(brands_2018)
elif selection == '2':
	brands_2019 = set([item[0] for item in sale2019])
	brands_2018 = set([item[0] for item in sale2018])
	common_brands = sorted(list(brands_2019.intersection(brands_2018)))
	print(common_brands)
elif selection == '3':
	brands_2019 = set([item[0] for item in sale2019])
	brands_2018 = set([item[0] for item in sale2018])
	all_brands = sorted(list(brands_2019.union(brands_2018)))
	print(all_brands)
elif selection == '4':
	brands_2019 = set([item[0] for item in sale2019])
	brands_2018 = set([item[0] for item in sale2018])
	new_brands = sorted(list(brands_2019.difference(brands_2018)))
	print(new_brands)
elif selection == '5':
	brands_2019 = set([item[0] for item in sale2019])
	brands_2018 = set([item[0] for item in sale2018])
	new_brands = sorted(list(brands_2019.difference(brands_2018)))
	dropped_brands = sorted(list(brands_2018.difference(brands_2019)))
	result = new_brands + dropped_brands
	print(result)