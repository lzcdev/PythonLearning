#/usr/bin/python
#coding:utf-8
__author__ = 'lzc'

import sys 
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import tool
import os

# 中文编码
reload(sys)  
sys.setdefaultencoding('utf8')  


class Spider:

	def __init__(self):
		self.siteURL = 'https://mm.taobao.com/json/request_top_list.htm'

	def getPage(self, page):
		url = self.siteURL + '?page=' + str(page)
		print url
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		soup = BeautifulSoup(response.read().decode('gbk'), 'lxml')
		return soup

	# 获取信息
	def getContents(self, page):
		contents = self.getPage(page)
		list_item = contents.select('div[class="list-item"]')
		content_list = []
		for item in list_item:
			
			detail_node = item.find('a')
			img_node = item.find('img')
			name_node = item.find('p', class_ = 'top').find('a')
			age_node = item.find('p', class_ = 'top').find('strong')
			address_node = item.find('span')
			career_node = item.select('p')[1].find('em')
			score_node = item.select('p')[1].find('strong')
			# 正则去掉开头的两个斜线
			img = re.sub(re.compile(r'//'),"https://",img_node['src'])
			detail = re.sub(re.compile(r'//'),"https://",detail_node['href'])
			
			# print img + "  " + detail + "  " + name_node.get_text() + "  " + age_node.get_text() + "  " + address_node.get_text() + "  " + career_node.get_text() + "  " + score_node.get_text()
			content_list.append([img,detail,name_node.get_text(),age_node.get_text(),address_node.get_text(),career_node.get_text(),score_node.get_text()])
		
			# print name_node.get_text()
			# print age_node.get_text()
			# print address_node.get_text()
			# print career_node.get_text()
			# print score_node.get_text()
		return content_list	

	# 获取个人详情页信息
	def getDetailPage(self,infoURL):
		return BeautifulSoup(urllib2.urlopen(urllib2.Request(infoURL)), 'lxml')

	#获取个人文字简介
	def getBrief(self,page):
		pass

	# 获取页面所有图片
	def getAllImg(self,page):
		images = page.select('#淘女郎')
		return images	

	# 保存图片
	def sageImg(self, imageURL, fileName):
		u = urllib.urlopen(imageURL)
		data = u.read()
		f = open(fileName, 'wb')
		f.write(data)
		f.close()

	# 保存头像
	def saveIcon(self,iconURL,name):
		splitPath = iconURL.split('.')
		fTail = splitPath.pop()
		fileName = name + '/icon.' + fTail
		self.sageImg(iconURL,fileName)

	# 保存文本
	def saveBrief(self, content, name):
		fileName = name + "/" + name + ".txt"
		f = open(fileName, "w+")
		print '正在偷偷保存她的个人信息为',fileName
		f.write(content)

	# 创建新目录
	def mkdir(self,path):
		path = path.strip()
		isExists = os.path.exists(path)
		if not isExists:
			print '创建名字叫做',path,'的文件夹'
			os.makedirs(path)
			return True
		else:
			print '名为',path,'的文件夹已经创建成功'
			return False	

	# 将一页MM信息保存起来
	def savePageInfo(self,pageIndex):
		contents = self.getContents(pageIndex)
		for item in contents:
			
			# print item[0] + item[2]
			print '发现一名模特,名字叫:%s,芳龄:%s,她在:%s,她的职业是:%s,她的个人地址是:%s' % (item[2],item[3],item[4],item[5],item[1])
			print '正在保存%s的信息' % item[2]
			# 个人详情页地址
			detailURL = item[1]
			print detailURL
			detailPage = self.getDetailPage(detailURL)
			# print detailPage
			# images = self.getAllImg(detailPage)
			# print images
			self.mkdir(item[2])
			self.saveIcon(item[0],item[2])
			

spider = Spider()
# spider.getContents(1)
spider.savePageInfo(1)					
