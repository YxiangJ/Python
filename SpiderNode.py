#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 11:02:42
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import re
import urllib
from bs4 import BeautifulSoup
from multiprocessing.managers import BaseManager
from multiprocessing import Process, Queue
from controlSpider import *

#HTML下载器
class HtmlDownloader(object):
	def download(self, url):
		if url is None:
			return None
		user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT)'
		headers = {'User-Agent':user_agent}
		r = requests.get(url,headers=headers)
		if r.status_code==200:
			r.encoding='utf-8'
			return r.text
		return None

#HTML解析器
class HtmlParser(object):
	def parser(self, page_url, html_cont):
		'''
		用于解析网页内容，抽取URL和数据
		:param page_url:下载页面的URL
		:param html_cont:下载的网页内容
		:return:返回URL和数据
		'''
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data

	def _get_new_urls(self, page_url, soup):
		'''
		抽取新的URL集合
		:param page_url:下载页面的URL
		:param soup:soup
		:return:返回新的URL集合
		'''
		new_urls = set()
		#抽取符合要求的a标记
		links = soup.find_all('a',href=re.compile(r'/view/\d+\.html'))
		for lik in links:
			#提取href属性
			new_url = link['href']
			#拼接成完整网址
			new_full_url = urllib.request.urljoin(page_url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, page_url, soup):
		'''
		抽取有效数据
		:param page_url:下载页面的URL
		:param soup:
		:return:返回有效数据
		'''
		data={}
		data['url']=page_url
		title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
		data['title']=title.get_text()
		summary = soup.find('div',class_='lemma-summary')
		#获取tag中包含的所有文本内容，包括子孙tag中的内容，并将结果作为Unicode字符串返回
		data['summary'] = summary.get_text()
		return data

#爬虫调度器
class SpiderWork(object):
	def __init__(self):
		#初始化分布式进程中工作节点的连接工作
		#实现第一步：使用BaseMa注册用于获取Queue的方法名称
		BaseManager.register('get_task_queue')
		BaseManager.register('get_result_queue')
		#实现第二步：连接到服务器
		server_addr = '127.0.0.1'
		print('Connect to server %s...' % server_addr)
		#注意保持端口和验证口令与服务进程设置的完全一致
		self.m = BaseManager(address=(server_addr, 8002), authkey='baike'.encode('utf-8'))
		#从网络连接
		self.m.connect()
		#实现第三步：获取Queue的对象
		self.task = self.m.get_task_queue()
		self.result = self.m.get_result_queue()
		#初始化网页下载器和解析器
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		print('init finish')

	def crawl(self):
		while True:
			try:
				if not self.task.empty():
					url = self.task.get()

					if url == 'end':
						print('控制节点通知爬虫节点停止工作...')
						#接着通知其他节点停止工作
						self.result.put({'new_urls':'end','data':'end'})
						return
					print('爬虫节点正在解析：%s'%url.encode('utf-8'))
					content = self.downloader.download(url)
					new_urls,data = self.parser.parser(url, content)
					self.result.put({'new_urls':new_urls,'data':data})
			except EOFError as e:
				print("连接工作节点失败")
				return
			except Exception as e:
				print(e)
				print('Crawl fail')
if __name__ == '__main__':
	spider = SpiderWork()
	spider.crawl()
		
