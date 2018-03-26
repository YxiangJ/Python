'''
UDP连接
1.创建Socket，绑定指定的IP和端口
2.直接发送数据和接收数据
3.关闭Socket
'''

import socket
#创建Socket，绑定指定的IP和端口
#SOCK_DGRAM指定了这个Socket的类型是UDP，绑定端口和TCP示例一样
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
while True:
	#直接发送数据和接收数据
	data,addr=s.recvfrom(1024)
	print('Received from %s:%s.'% addr)
	s.sendto(b'Hello,%s!'% data,addr)
