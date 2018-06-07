#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-24 15:37:30
# @Author  : YxiangJ (15751005410@139.com)
# @Link    : https://github.com/YxiangJ
# @Version : $Id$


import urllib.request
import http.cookiejar

cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cookie))
response = opener.open('http://www.zhihu.com', timeout=2)
for item in cookie:
    print(item.name + ':' + item.value)

'''
# selenium中cookie处理

driver.get("http://www.baidu.com")
cookie = {'name':'foo', 'value':'bar'}
driver.add_cookie(cookie)
driver.get_drivers()
'''

'''
# cookie登录
def save_session(session):
	# 将session写入文件:session.txt
	with open('session.txt', 'wb') as f:
		pickle.dump(session.headers, f)
		pickle.dump(session.cookie.get_dict(), f)
		print('[+]将session写入文件: session.txt')


def load_session(session):
	# 加载session
	with opne('session.txt', 'rb') as f:
		headers = pickle.load(f)
		cookies = pickle.load(f)
		return headers, cookies
'''
