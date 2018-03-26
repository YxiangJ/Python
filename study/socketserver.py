#socket服务器
#导入socket，sys模块
import socket
import sys


#创建socket对象
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#读取本机主机名
host = socket.gethostname()
port = 9999
#绑定端口号
serversocket.bind((host, port))
#设置最大连接数，超过后排队
serversocket.listen(5)
#建立客户端连接
while True:
	clientsocket,addr = serversocket.accept()
	print("连接地址: %s" % str(addr))
	msg = '首次使用socket网络编程'+"\r\n"
	clientsocket.send(msg.encode('utf-8'))
	clientsocket.close()