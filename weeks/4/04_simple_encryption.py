"""
任务描述
用户在一行中输入一个包括大小写字母和数字的字符串，编程实现字符串加密。加密规则如下：

1. 将字符串中的大写字母用字母表中该字母后的第5个字母替代
2. 将字符串中的小写字母用字母表中该字母后的第3个字母替代
3. 字符串中的其他字符原样输出

输入格式
输入一个至少包含一个字母的字符串

输出格式
输出加密后的字符串

示例 1
输入：
Life is short, you need Python!    

输出：
Qlih lv vkruw, brx qhhg Ubwkrq!
"""

string_to_encrypt = input()
encrypted_string = ""

for char in string_to_encrypt:
	if char.isupper():
		encrypted_string += chr((ord(char) - ord('A') + 5) % 26 + ord('A'))
	elif char.islower():
		encrypted_string += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
	else:
		encrypted_string += char

print(encrypted_string)