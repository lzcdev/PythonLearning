#!/usr/bin/python
#coding:utf-8

import re
import urllib
import urllib2
import requests
import os
import sys

# 中文编码
reload(sys)  
sys.setdefaultencoding('utf8')  

class Spider:

	def __init__(self):
		self.url = 'http://www.jikexueyuan.com/course/'
		self.folder_name = 'pic_folder'

	def getHtml(self,url):
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read()

	# 创建目录
	def mkdir(self,name):
		folder_name = name.strip()
		isExists = os.path.exists(folder_name)
		if not isExists:
			print '名字为%s的文件夹创建成功' % folder_name
			os.mkdir(folder_name)
			return True
		else:
			print '名字为%s的文件夹已存在' % folder_name
			return False

	# 写入图片
	def saveImg(self,pic,i):
		fp = open(self.folder_name +'/' + str(i) + '.jpg', 'wb')
		fp.write(pic.content)
		print '写入第%s张成功' % i
		fp.close()	

	def start(self,pageIndex):
		self.mkdir(self.folder_name)
		if pageIndex > 97:
			print '截止到目前，最多97页'
			return	
		i = 0
		for index in range(1,pageIndex+1):
			self.url = self.url + '?pageNum=' + str(index)
			html = self.getHtml(self.url)
			pic_urls = re.findall('<img src="(.*?)" class="lessonimg"',html)
			for pic_url in pic_urls:
				print pic_url
				pic = requests.get(pic_url)
				self.saveImg(pic,i)
				i += 1			

spider = Spider()
spider.start(5)

