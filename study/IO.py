'''try:
    f=open(r'e:\workspace\。。。.txt')
    print(f.read())
finally:
    if f:
        f.close()'''
import os

with open(r'E:\workspace\。。。.txt','rb') as fileReader:
    for line in fileReader.readlines():
        print (line.strip())

#os.getcwd()
