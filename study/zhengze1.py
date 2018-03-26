import re
#将正则表达式编译成pattern对象
pattern=re.compile(r'\d+')
#使用re.match匹配文本，获得匹配结果，无法匹配时返回none
result1=re.match(pattern, '192abc')
if result1:
	print(result1.group())
else:
	print('匹配失败1')
result2=re.match(pattern, 'abc192')
if result2:
	print(result2.group())
else:
	print('匹配失败2')
#使用re.search匹配文本，获得匹配结果，无法匹配时返回none
result1=re.search(pattern, 'abc192edf')
if result1:
	print(result1.group())
else:
	print('匹配失败1')

#split将string分割后返回列表
print(re.split(pattern, 'A1B2C3D4'))

#findall搜索整个string，以列表形式返回能匹配的全部子串

print(re.findall(pattern, 'A1B2C3D4'))

#finditer 以迭代器形式返回能匹配的全部Match对象
matchiter=re.finditer(pattern, 'A1B2C3D4')
for match in matchiter:
	print(match.group())

#使用repl替换string中没一个匹配的子串后返回替换后的字符串
p=re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')	#使用名称引用
s='i say,hello world!'
print(p.sub(r'\g<word2> \g<word1>', s))
p=re.compile(r'(\w+) (\w+)')	#使用编号
print(p.sub(r'\2 \1', s))
def func(m):
	return m.group(1).title()+' '+m.group(2).title()
print(p.sub(func, s))


#subn返回sub替换次数
print(p.subn(r'\2 \1', s))
print(p.subn(func, s))