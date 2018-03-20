#!/usr/bin/python
#coding:utf-8
__author__ = 'lzc'

import sys  
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

# 中文编码
reload(sys)  
sys.setdefaultencoding('utf8')  

class QSBK:

	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'
		self.headers = {'User-Agent': self.user_agent}
		self.stories = []
		self.enable = False

	# 传入第几页，返回页面数据列表
	def getPage(self, pageIndex):
		try:
			url = 'https://www.qiushibaike.com/hot/page/' + str(pageIndex)
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request)
			soup = BeautifulSoup(response.read(), 'lxml')
			return soup
		except urllib2.URLError, e:
			if hasattr(e, 'reason'):
				print '连接糗事百科失败，错误原因：' + e.reason
			return None	

	# 传入第几页，返回数据（已处理）			
	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print '页面加载失败'
			return None
		node = pageCode.select('div[class="col1"] > div')
		pageStories = []
		for node_item in node:
 			# 姓名
			author = node_item.find('h2')
			# 内容
			content = node_item.find('span')
			# 年龄
			age = node_item.find('div', class_ = 'author clearfix').find('div')
			# 性别
			gender_class = node_item.find('div', class_ = 'author clearfix').find('div')
			# 点赞数（好笑）
			stats_vote = node_item.find('span', class_ = 'stats-vote').find('i')
			# 评论数
			stats_comments = node_item.find('span', class_ = 'stats-comments').find('i')  
			
			# 姓名
			if author is not None:
				pageStories.append([author.get_text().strip(), stats_vote.get_text().strip(), stats_comments.get_text().strip(), content.get_text().strip()])
			else:
				return 'None'
		return pageStories
		

	# 加载并提取页面内容
	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	# 每次回车打印输出一个段子
	def getOneStory(self, pageStories, page):
		
		for story in pageStories:
			input = raw_input()
	
			self.loadPage()
			if input == "Q":
				self.enable = False
				return
			print '姓名：%s 点赞数：%s 评论数：%s 内容：%s' % (story[0], story[1], story[2], story[3])

		
	# 开始方法
	def start(self):
		print '正在读取糗事百科，按回车查看新段子，Q退出'
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories, nowPage)		
			
spider = QSBK()
spider.start()


