"""# first example
import os
import os.path

'''获取指定目录及其子目录下的py文件路径说明：1用于存储找到的py文件路径
get_py函数，递归查找并存储py文件于l'''
l=[]
def get_py(path,l):
    fileList=os.listdir(path)   #获取path目录下所有文件
    for filename in fileList:
        pathTmp=os.path.join(path,filename)  #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):  #如果是目录
            get_py(pathTmp,l)       #则递归查找
        elif filename[-3:].upper()=='.PY':  #不是目录,则比较后缀名
            l.append(pathTmp)
path=input('请输入路径:').strip()
get_py(path,l)
print('在%s目录及其子目录下找到%d个py文件\n分别为:\n'%(path,len(l)))
for filepath in l:
    print(filepath+'\n')
"""

import os

def search_file(start_dir,target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext=os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd()+os.sep+each_file+os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file,target)#递归调用
            os.chdir(os.pardir)#递归调用后切记返回上一层目录

start_dir= input('请输入待查找的初始目录：')
program_dir=os.getcwd()

target=['.mp4','.avi','.rmvb']
vedio_list=[]

search_file(start_dir,target)

f=open(program_dir+os.sep+'vedioList.txt','w')
f.writelines(vedio_list)
f.close()
