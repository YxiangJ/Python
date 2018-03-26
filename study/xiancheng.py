'''
import time
import threading


def loop():
	print('thread {} is running...'.format(threading.current_thread().name))
	n = 0
	while n < 5:
		n += 1
		print('thread {} >>> {}'.format((threading.current_thread().name),n))
		time.sleep(1)
	print('thread {} ended.'.format(threading.current_thread().name))
print('thread {} is running...'.format(threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread {} ended.'.format(threading.current_thread().name))
'''

'''
#用threading模块创建多线程
import random
import time,threading
#新线程执行的代码
def thread_run(urls):
	print('Current %s is running...' % threading.current_thread().name)
	for url in urls:
		print('%s---->>> %s' % (threading.current_thread().name,url))
		time.sleep(random.random())
	print('%s ended.'% threading.current_thread().name)
print('%s is running...' % threading.current_thread().name)
t1=threading.Thread(target=thread_run,name='Thread_1',args=(['url_1','url_2','url_3'],))
t2=threading.Thread(target=thread_run,name='Thread_2',args=(['url_4','url_5','url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)
'''


'''
#从threading.Thread继承创建线程类
import random
import time,threading
#新线程执行的代码
class myThread(threading.Thread):
 	def __init__(self, name,urls):
 		threading.Thread.__init__(self,name=name)
 		self.urls = urls
 	def run(self):
 		print('Current %s is running...' % threading.current_thread().name)
 		for url in self.urls:
 			print('%s---->>> %s' % (threading.current_thread().name,url))
 			time.sleep(random.random())
 			print('%s ended.' % threading.current_thread().name)
print('%s is running...' % threading.current_thread().name)
t1=myThread(name='Thread_1',urls=['url_1','url_2','url_3'])
t2=myThread(name='Thread_2',urls=['url_4','url_5','url_6'])
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)
'''

'''
#线程锁
import threading
import time

balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		#先要获取锁
		lock.acquire()
		try:
			#放心的改吧
			change_it(n)
		finally:
			#释放锁
			lock.release()
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''

#'''
#线程同步
import threading
mylock=threading.RLock()
num=0
class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self, name):
		threading.Thread.__init__(self,name=name)
	
	def run(self):
		global num
		while True:
			mylock.acquire()
			print('%s locked,Number: %d'% (threading.current_thread().name,num))
			if num>=4:
				mylock.release()
				print('%s released,Number: %d'%(threading.current_thread().name,num))
				break
			num+=1
			print('%s released,Number: %d'%(threading.current_thread().name,num))
			mylock.release()


if __name__=='__main__':
	thread1=myThread('Thread_1')
	thread2=myThread('Thread_2')
	thread1.start()
	thread2.start()
#'''
