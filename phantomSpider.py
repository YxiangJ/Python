#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 16:47:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Ie()
driver.get("http://www.baidu.com")
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫." not in driver.page_source
driver.close()
