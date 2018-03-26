import pickle
import os


datafile = 'person.data'
line = '======================================='
message = '''
=======================================
欢迎进入通讯录:
    输入1查看通讯录
    输入2添加联系人
    输入3编辑联系人
    输入4删除联系人
    输入5查找联系人
    输入6查看联系人列表
    输入0退出
=======================================
'''
print(message)

class Person(object):
	"""通讯录联系人"""
	def __init__(self, name, number):
		self.name = name
		self.number = number

	#获取数据
	def get_data(filename=person.data):
		#文件存在且不为空
		if os.path.exists(filename) and os.path.getsize(filename):
			with open(filename,'rb') as f:
				return pickle.load(f)
		return None
	#写入数据
	def set_data(name, number, filename=datafile):
		
		personList = {} if get_data() == None else get_data()

		with open(filename,'wb') as f:
			personList[name] = Person(name, number)
			pickle.dump(personList, f)

	#保存字典格式的数据到文件
	def save_data(dictPerson, filename=datafile):
		with open(filename,'wb') as f:
			pickle.dump(dictPerson, f)

	#显示所有联系人
	def show_all():
		personList = get_data()
		if personList:
			for v in personList.values():
				print(v.name,v.number)
			print(line)
		else:
			print('没有这个联系人，请添加联系人')
			print(line)

	#添加联系人
	def add_person(name,number):
		set_data(name,number)
		print('成功添加联系人')
		print(line)

	#编辑联系人
	def edit_person(name,number):
		personList = get_data()
		if personList:
			personList[name] = Person(name, number)
			save_data(personList)
			print('编辑联系人成功')
			print(line)

	#删除联系人
	def delete_person(name):
		personList = get_data()
		if personList:
			if name in personList:
				del personList[name]
				save_data(personList)
				print('删除联系人成功')
			else:
				print(name,'联系人不在通讯录中')
			print(line)

	#搜索联系人
	def search_person(name):
		personList = get_data()
		if personList:
			if name in personList.keys():
				print(personList.get(name).name, personList.get(name).number)
			else:
				print('该联系人不存在',name)
			print(line)
	while True:
		num = input('>>')

	if num == '1':
		print('show all personList:')
		show_all()
	elif num == '2':
		print('add person:')    
		name = input('input name>>')
		number = input('input number>>')
		add_person(name,number)
	elif num == '3':
		print('edit person:')
		name = input('input name>>')
		number = input('input number>>')
		edit_person(name,number)
	elif num == '4':
		print('delete person:')
		name = input('input name>>')
		delete_person(name)
	elif num == '5':
		print('search :')
		name = input('input name>>')
		search_person(name)
	elif num == '6':
		print(message)
	else:
		print('input error, please retry')


		
