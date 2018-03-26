'''# Fibonacci series:斐波那契数列
a,b=0,1
while b<1000:
    print(b,end=',')
    a,b=b,a+b'''

#递归方式的斐波那契数列
n=int(input('请输入一个整数:'))    
def fab(n):
    if n<1:
        print('输入错误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
result=[]
for i in range(1,n+1):
    result.append(fab(i))

print(result)
