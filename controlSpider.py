#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 08:57:25
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
# 控制节点（控制调度器，URL管理器，数据存储器）爬虫节点（爬虫调度器，HTML下载器，HTML解析器）

import os
import pickle
import hashlib
import codecs
import time
from multiprocessing.managers import BaseManager
from multiprocessing import Process
from queue import Queue
from SpiderNode import *

# URL管理器


class UrlManager(object):

    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')  # 未爬取url集合
        self.old_urls = self.load_progress('old_urls.txt')  # 已爬取url集合

    def has_new_url(self):
        '''
        获取一个未爬取的URL
        ：return：
        '''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''
        获取一个未爬取的URL
        ：return：
        '''
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url.encode('utf-8'))
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self, url):
        '''
        将新的URL添加到未爬取的URL集合中
        ：param url：单个URL
        ：return:
        '''
        if url is None:
            return
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        将新的URL添加到URL集合中
        ：param urls:url集合
        ：return:
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        '''
        获取未爬取URL集合的大小
        ：return:
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        获取已经爬取URL集合的大小
        ：return:
        '''
        return len(self.old_urls)

    def save_progress(self, path, data):
        '''
        :param path:文件路径
        :param data:数据
        :return:
        '''
        with open(path, 'wb') as f:
            pickle.dump(data, f)

    def load_progress(self, path):
        '''
        从本地文件加载进度
        :param path:文件路径
        :return:返回set集合
        '''
        print('[+] 从文件加载进度：%s' % path)
        try:
            with open(path, 'rb') as f:
                tmp = pickle.load(f)
                return tmp
        except Exception as e:
            print('[!] 无进度文件，创建：%s' % path)
        return set()

# 数据存储器


class DataOutput(object):

    def __init__(self):
        self.filepath = 'bake_%s.html' % (
            time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        '''
        将HTML头写进去
        ：return
        '''
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.close()

    def output_html(self, path):
        '''
        将数据写入HTML文件名中
        :param path:文件路径
        :return
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.close()

    def output_end(self, path):
        '''
        输出HTML结束
        ：param path文件存储路径
        :return:
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

# 控制调度器


class NodeManager(object):
    # 分布式管理器

    def start_Manager(self, url_q, result_q):
        '''
        创建一个分布式管理器
        :param url_q:url队列
        :param result_q:结果队列
        :return:
        '''
        # 把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象
        # 将Queue对象在网络中暴露
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_resut_queue', callable=lambda: result_q)
        # 绑定端口8001，设置验证口令"baike"。相当于对象的初始化
        manager = BaseManager(address=('127.0.0.1', 8001),
                              authkey='baike'.encode('utf-8'))
        # 返回manager对象
        return manager

    # URL管理进程
    def url_manager_proc(self, url_q, conn_q, root_url):
        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while (url_manager.has_new_url()):
                # 从URL管理器获取新的URL
                new_url = url_manager.get_new_url()
                # 将新的URL发给工作节点
                url_q.put(new_url)
                print('old_url=', url_manager.old_url_size())
                # 加一个判断条件，当爬取2000个链接后就关闭，并保存进度
                if (url_manager.old_url_size() > 2000):
                    # 通知爬行节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知！')
                    # 关闭管理节点，同时存储set状态
                    url_manager.save_progress(
                        'new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress(
                        'old_urls.txt', url_manager.old_urls)
                    return
            # 将从result_solve_proc获取到的url添加到URL管理器
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_urls(urls)
            except Exception as e:
                time.sleep(0.1)  # 延时休息

    # 数据提取进程
    def result_solve_proc(slef, result_q, conn_q, store_q):
        while (True):
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        # 结果分析进程接收通知然后结束
                        print('结果分析进程接收通知然后结束！')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])  # url为set类型
                    store_q.put(content['data'])  # 解析出来的数据为dict类型
                else:
                    time.sleep(0.1)  # 延时休息
            except Exception as e:
                time.sleep(0.1)  # 延时休息

    # 数据存储进程
    def store_proc(self, store_q):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('存储进程接受通知然后结束！')
                    output.output_end(output.filepath)

                    return
                output.store_data(data)
            else:
                time.sleep(0.1)


if __name__ == '__main__':
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()
    # 创建分布式管理器
    node = NodeManager()
    manager = node.start_Manager(url_q, result_q)
    # 创建URL管理进程、数据提取进程、数据存储进程
    url_manager_proc = Process(target=node.url_manager_proc, args=(
        url_q, conn_q, 'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc = Process(
        target=node.result_solve_proc, args=(result_q, conn_q, store_q,))
    store_proc = Process(target=node.store_proc, args=(store_q,))
    # 启动三个进程和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()
