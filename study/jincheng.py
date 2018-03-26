'''
#多进程
import os
from multiprocessing import Process

#子进程执行的代码
def run_proc(name):
    print('Child process %s (%s) Running...'%(name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p=Process(target=run_proc(i),args=(str(i),))
        print('Process will start.')
        p.start()
    p.join()
    print('Process end.')

'''
'''
#Pool池多进程
from multiprocessing import Pool
import os,time,random

def run_task(name):
    print("Task %s (pid=%s) is running..." % (name,os.getppid()))
    time.sleep(random.random()*3)
    print("Task %s end."% name)

if __name__=='__main__':
    print('Current process %s.' % os.getppid())
    p=Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task(i),args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
'''
'''
#进程同步锁

from multiprocessing import Process,Lock
import time
import random
import os

def work(filename,lock):    #买票
    #lock.acquire()
    with lock:
        with open(filename,encoding='utf-8') as f:
            dic=json.loads(f.read())
            #print('剩余票数：%s'% dic['count'])
            if dic['count']>0:
                dic['count']-=1
                time.sleep(random.randint(1,3)) #模拟网络延迟
                with open(filename,'w',encoding='utf-8')as f:
                    f.write(json.dumps(doc))
                print('%s 购票成功'%os.getpid())
            else:
                print('%s 购票失败'%os.getpid())
        #lock.release()
if __name__=='__main__':
    lock=Lock()
    p_1=[]
    for i in range(10):
        p=Process(target=work(i,lock),args=('db',lock))
        p_1.append(p)
        p.start()
    for p in p_1:
        p.join()
        
    print('主线程')
'''

'''
# 进程间通信

from multiprocessing import Process, Queue
import os
import time
import random

# 写数据进程执行的代码


def proc_write(q, urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())

# 读数据进程执行的代码


def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:

        url = q.get(True)
        print('Get %s from queue.' % url)

if __name__ == '__main__':  # 父进程创建queue，并传给各个子进程
    q = Queue()
    proc_writer1 = Process(target=proc_write(q,['url_1', 'url_2', 'url_3']), args=(
        q, ['url_1', 'url_2', 'url_3']))
    proc_writer2 = Process(target=proc_write(q,['url_1', 'url_2', 'url_3']), args=(
        q, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read(q), args=(q,))
    # 启动子进程proc_writer，写入：
    proc_writer1.start()
    proc_writer2.start()
    # 启动子进程proc_reader,读取：
    proc_reader.start()
    # 等待proc_writer结束：
    proc_writer1.join()
    proc_writer2.join()
    # proc_reader进程里是死循环，无法等待其结束，只能强行中止：
    proc_reader.terminate()

'''
'''
from multiprocessing import Process,Queue
import time
q=Queue(3)


#put ,get ,put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
print(q.full()) #满了

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了
'''
'''
#Queue进程间通信
from multiprocessing import Process,Queue
import time,random,os

def consumer(q):
    while True:
        time.sleep(random.randint(1,3))
        res=q.get()
        if res is None:break
        print('消费者拿到了：%s' %res)

def producer(seq,q):
    for item in seq:
        time.sleep(random.randint(1,3))
        print('生产者生产了：%s' %item)

        q.put(item)

if __name__ == '__main__':
    q=Queue()
    consumer = consumer(q)
    c=Process(target=consumer,args=(q,))
    c.start()

    producer(('包子%s' %i for i in range(5)),q)
    q.put(None)
    c.join()
    print('主线程')
'''
'''
import multiprocessing
import random
import time,os

def proc_send(pipe,urls):
    for url in urls:
        print("Process(%s) send: %s" % (os.getpid(),url))
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print("Process(%s) recv: %s" % (os.getpid(),pipe.recv()))
        time.sleep(random.random())
if __name__=="__main__":
    pipe=multiprocessing.Pipe()
    p1=multiprocessing.Process(target=proc_send,args=(pipe[0],['url_'+str(i) for i in range(10)]))
    p2=multiprocessing.Process(target=proc_recv,args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

'''
'''
import subprocess


print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit Code:',r)
'''
'''
#分布式进程
#服务进程
import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#从BaseMan继承的QueueManager
class QueueManager(BaseManager):
    pass
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

#把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=return_task_queue)
QueueManager.register('get_result_queue', callable=return_result_queue)
#绑定端口5000，设置验证码'abc'
manager = QueueManager(address=('127.0.0.1', 5000),authkey=b'abc')
#启动Queue
manager.start()
#获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
#放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task {}...'.format(n))
    task.put(n)
print('Try get results...')
#从result队列读取结果
for i in range(10):
    r = result.get(timeout=10)
    print('Result:{}'.format(r))
#关闭
manager.shutdown()
print('master exit.')

'''
#任务进程
import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager
class QueueManager(BaseManager):
    pass

#由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#连接到服务器，也就是运行task_master.py的机器
server_addr = '127.0.0.1'
print('Connect to server {}...'.format(server_addr))
#端口和验证码注意保持task_master.py与设置的完全一致
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
#从网络连接
m.connect()
#获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
#从task队列取任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task {} * {}...'.format(n,n))
        r = '{} * {} = {}'.format(n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
#处理结束
print('worker exit.')

