#!/usr/bin/python
#coding:utf-8
__author__ = 'lzc'

import urllib
import urllib2
import re
from bs4 import BeautifulSoup

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'
headers = {'User-Agent': user_agent}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	soup = BeautifulSoup(response.read(), 'lxml')
	node = soup.select('div[class="col1"] > div')
	print type(node)
	for node_item in node:
		author = node_item.find('h2')
		content = node_item.find('span')
		age = node_item.find('div', class_ = 'author clearfix').find('div')
		print author.get_text()
		print content.get_text()
		if age is not None:
			print age.get_text()		

except urllib2.URLError, e:
	if hasattr(e, 'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason		
