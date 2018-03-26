"""
#HTTP处理

#get请求的HTTP的python实现
#q请求头headers处理
import urllib.request
'''
response=urllib.request.urlopen('https://www.zhihu.com')
html=response.read()
'''
url='http://www.xxxxxx.com/login'
user_agent='Mozilla/4.0(compatible;MSIE5.5;Windows NT)'
referer='http://www.xxxxxx.com'
postdata={'username':'qiye','password':'qiye_pass'}
data=urllib.request.urlencode(postdata)
req=urllib.request.Request(url)
#将user_agent，referer写入头信息
req.add_header('User-Agent',user_agent)
req.add_header('Referer'.referer)
req.add_data(data)
response=urllib.request.urlopen(req)
html=response.read()

'''
#请求
request=urllib.request.Request('https://www.zhihu.com')
#响应
response=urllib.request.urlopen(request)
html=response.read()
print(html)
'''

'''
#post请求的HTTP的python实现
import urllib
url='http://www.xxxxxx.com/login'
user_agent='Mozilla/4.0(compatible;MSIE5.5;Windows NT)'
referer='http://www.xxxxxx.com'
postdata={'username':'qiye','password':'qiye_pass'}
#将user_agent，referer写入头信息
headers=('User-Agent':user_agent,'Referer':referer)
data=urllib.request.urlencode(postdata)
req=urllib.request.Request(url,data)
response=urllib.request(req)
html=response.read()
'''
"""


#Cookie处理
import urllib
import cookielib

cookie=cookielib.CookieJar()
opener=urllib.build_opener(urllib.HTTPCookieProcessor(cookie))
response=opener.open('http://www.zhihu.com')
for item in cookie:
	print(item.name+':'+item.value)

