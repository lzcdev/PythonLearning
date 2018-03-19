#!/usr/bin/python
#coding:utf-8
__author__ = 'lzc'

import urllib
import urllib2

#请求百度首页，失败
# request = urllib2.Request("https://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()


# 登录csdn,失败
# values = {"username":"XXX", "password": "XXX"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()


# 登录知乎成功,修改对应账号密码
# import urllib  
# import urllib2  
# url = 'https://www.zhihu.com/signup?next=%2F'
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'  
# values = {'username' : 'XXX',  'password' : 'XXX' }  
# headers = { 'User-Agent' : user_agent }  
# data = urllib.urlencode(values)  
# request = urllib2.Request(url, data, headers)  
# response = urllib2.urlopen(request)  
# page = response.read() 
# print page


# requset = urllib2.Request('http://www.x.com')
# try:
#     urllib2.urlopen(requset)
# except urllib2.URLError, e:
#     print e.reason


# cookie
# import cookielib

# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)

# #声明一个CookieJar对象实例来保存cookie
# # cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('https://www.baidu.com')

# cookie.save(ignore_discard=True, ignore_expires=True)

# # print response.read()
# for item in cookie:
# 	print 'Name = ' + item.name 
# 	print 'Value + ' + item.value


# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# print cookie
# req = urllib2.Request("https://www.baidu.com")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()


#正则表达式
import re

# pattern = re.compile(r'hello')

# result1 = re.match(pattern, 'hello')
# result2 = re.match(pattern, 'helloo lzc')
# result3 = re.match(pattern, 'helo lzc')
# result4 = re.match(pattern, 'hello lzc')

# if result1:
# 	print result1.group()
# else:
# 	print '1匹配失败'

# if result2:
# 	print result2.group()
# else:
# 	print '2匹配失败'

# if result3:
# 	print result3.group()
# else:
# 	print '3匹配失败'	

# if result4:
# 	print result4.group()
# else:
# 	print '4匹配失败'		

# 匹配如下内容：单词+空格+单词+任意字符
# m = re.match(r'(\w+) (\w+)(?P.*)', 'hello world')

# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
# print "m.group():", m.group()
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

# pattern = re.compile(r'\d+')
# print re.findall(pattern, 'one1two2three3four4five5')


# Beautiful Soup
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
# print soup.prettify()
# tags
print soup.title  
print soup.head
print soup.a
print soup.p
print type(soup.a)
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p['class']
print soup.p.get('class')
soup.p['class']='newClass'
print soup.p
del soup.p['class']
print soup.p


# NavigableString
# print soup.p.string
# print type(soup.p.string)

# # BeautifulSoup
# print type(soup.name)
# print soup.name
# print soup.attrs


# # Comment
# print soup.a
# print soup.a.string
# print type(soup.a.string)
# if type(soup.a.string)==bs4.element.Comment:
# 	print soup.a.string


# print soup.head.contents
# print soup.head.contents[0]

# print soup.head.children
# for child in soup.body.children:
# 	print child

# for child in soup.descendants:
# 	print child


# 搜索文档树
print soup.find_all('b')
for tag in soup.find_all(re.compile("^b")):
	print tag.name

def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(has_class_but_no_id)		
















