#/usr/bin/python
#coding:utf-8
__author__ = 'lzc'


import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import sys

# 中文编码
reload(sys)  
sys.setdefaultencoding('utf8')  

# 处理页面标签的工具类
class Tool:
	# 去除img标签，7位长空格
	removeImg = re.compile('<img.*> | {7}')
	# 删除超链接标签
	removeAddr = re.compile('<a.*?> | </a>')
	# 把换行标签替换为\n
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
	# 将表格制表<td>替换为\t
	replaceTD = re.compile('<td>')
	# 把段落开头换为\n加空两格
	repalcePara = re.compile('<p.*?>')
	# 将换行符或双换行符替换为\n
	repalceBR = re.compile('<br><br>|<br>')
	# 将其余标签剔除
	removeExtraTag = re.compile('<.*?>')

	def replace(self, x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.repalcePara,"\n    ",x)
		x = re.sub(self.repalceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		# strip()将前后多余的内容删除
		return x.strip()


class BDTB:

	def __init__(self, baseUrl, see_lz, floorTag):
		self.baseUrl = baseUrl
		self.see_lz = '?see_lz='+str(see_lz)
		self.tool = Tool()
		# 文件写入对象
		self.file = None
		self.floor = 1
		self.defaultTitle = '百度贴吧'
		self.floorTag = floorTag

	# 传入页码，获取该页帖子的代码
	def getPage(self, pageNum):
		try:
			url = self.baseUrl + self.see_lz + '&pn=' + str(pageNum)
			# print url
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			soup = BeautifulSoup(response, 'lxml')
			# print response.read()
			return soup
		except urllib2.URLError, e:
			if hasattr(e, 'reason'):
				print '连接百度贴吧失败，错误原因',e.reason
				return None

	# 提取页面标题
	def getTitle(self, page):
		soup = self.getPage(1)
		title = soup.find('div', class_ = 'core_title_wrap_bright clearfix').find('h3')
		if title:
			return title.get_text().strip()
		else:
			return None	

	# 提取帖子一共有多少页
	def getPageNum(self, page):
		soup = self.getPage(1)
		pageNum = soup.find('li', class_ = 'l_reply_num').select('span')[1]
		if pageNum:
			return pageNum.get_text().strip()
		else:
			return None	

	# 提取每一层楼的内容，传入页面内容
	def getContent(self, page):
		soup = self.getPage(page)
		content = soup.select('cc > div')
		# print content[0]
		contents = []
		for item in content:
			content = '\n' + self.tool.replace(item.get_text()) + '\n'
			contents.append(content)
			# print floor,'楼-------------------------------------------------------------------\n'
			# print self.tool.replace(item.get_text())	
		return contents

	def setFileTitle(self, title):
		if title is not None:
			self.file = open(title + '.txt','w+')
		else:
			self.file = open(self.defaultTitle + '.txt','w+')

	def writeData(self, contents):
		# 向文件写入每一层楼的信息
		for item in contents:
			if self.floorTag == 1:
				floorLine = '\n' + str(self.floor) + '楼<----------------------->我是分割线<----------------------->\n'				
				self.file.write(floorLine)
			self.file.write(item)
			self.floor += 1

	def start(self):
		print '开始写入，请等待...'
		pageNum = self.getPageNum(1)
		title = self.getTitle(1)
		self.setFileTitle(title)
		if pageNum == None:
			print 'URL 已经失效，请重试'
			return
		try:
			print '该帖子共有' + str(pageNum) + '页'
			for i in range(1, int(pageNum)+1):
				print '正在写入第' + str(i) + '页数据'
				contents = self.getContent(i)
				self.writeData(contents)
		except IOError, e:
			print '写入异常，原因：' + e.message
		finally:
			print '写入任务完成'

# print '请输入帖子代号'
baseUrl = 'https://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1, 1)
bdtb.start()


























