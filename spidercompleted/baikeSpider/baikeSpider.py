#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-30 15:54:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

class UrlManager(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def has_new_url(self):
		return self.new_url_size()!=0

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self,urls):
		if urls is None or len(urls)==0:
			return
		for uel in urls:
			self.add_new_url(url)

	def new_url_size(self):
		return len(self.new_urls)

	def old_url_size(self):
		return len(self.old_urls)

class HtmlDownloader(object):

	def download(self,url):
		if url is None:
			return None
		user_agent='Mozilla/4.0 (compatible;MSIE 8.0;Window NT)'
		headers={'User-Agent':user_agent}
		r=requests.get(url,headers=headers)
		if r.status_code==200:
			r.encoding='utf-8'
			return r.text
		return None
		