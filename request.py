#!/usr/bin/python
#coding:utf-8

import requests
import json
# import ssl

# response = requests.get('https://www.baidu.com')
# print type(response)
# print response.status_code
# print type(response.text)
# # print response.text
# response.encoding = 'utf-8'
# print response.text
# print response.cookies
# print response.content
# print response.content.decode('utf-8')


# url = 'http://httpbin.org/get'
# data = {
# 	'name': 'lzc',
# 	'age': '26'
# }
# response = requests.get(url,params=data)
# print response.url
# print response.text
# print type(response.json())

# # 登录知乎
# url = 'https://www.zhihu.com/'
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
# }
# response = requests.get(url,headers=headers)
# response.encoding = 'utf-8'
# # print response.text
# print response.content


# # post
# url = 'http://httpbin.org/post'
# data = {
# 	'name': 'lzc',
# 	'age': '26'
# }
# response = requests.post(url,data=data)
# print response.text


# # 响应
# response = requests.get('http://www.baidu.com')
# print response.headers
# print response.cookies

# # 状态码
# response = requests.get('http://www.jianshu.com/404.html')
# if response.status_code != requests.codes.ok:
# 	print '404'

# response = requests.get('http://www.jianshu.com')	
# if response.status_code == 200:
# 	print '200'


# 高级操作
# url = 'http://httpbin.org/post'
# files = {
# 	'files': open('0.jpg','rb')
# }
# response = requests.post(url,files=files)
# print response.text


# 获取cookie
# response = requests.get('http://www.baidu.com')
# print response.cookies
# for key,value in response.cookies.items():
# 	print key, '==', value


# 会话维持
# session = requests.session()
# session.get('http://httpbin.org/cookies/set/number/12456')
# response = session.get('http://httpbin.org/cookies')
# print response.text

# 证书验证
# 1.无证书访问,消除验证证书警报
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn',verify=False)
# print response.status_code
# print response.text


# 代理设置
# proxies = {
# 	'http': 'http://127.0.0.1:9743',
# 	'https': 'https://127.0.0.1:9743',
# }
# response = requests.get('https://www.taobao.com',proxies=proxies)
# print response.status_code

# 超时设置
# from requests.exceptions import ReadTimeout

# try:
# 	response = requests.get('http://httpbin.org/get',timeout=0.5)
# 	print response.status_code
# except ReadTimeout:
# 	print 'Timeout'


# from requests.packages import urllib3
# urllib3.disable_warnings()
# r = requests.get('https://api.github.com/events')
# print r.status_code
# print r.json()































