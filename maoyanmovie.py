#!/usr/bin/python
#coding: utf-8

__author__ = 'lzc'

import requests
import re
from requests.exceptions import RequestException
import os

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

class Spider:

	def __init__(self):
		self.url = 'http://maoyan.com/board/4'
		pass

	def get_one_page(self,url):
		try:
			headers = {
				'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
			}
			response = requests.get(url,headers=headers)
			if response.status_code == 200:
				# print response.text
				return response.text
			else:
				return None
		except RequestException:
			return None	

	def parse_one_page(self,url):
		list = []
		html = self.get_one_page(url)
		pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
                      +'<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">'
                      +'(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>',re.S)
		items = re.findall(pattern,html)
		return items	


	# 创建目录
	def mkdir(self):
		folder_name = 'movie'
		isExists = os.path.exists(folder_name)
		if not isExists:
			print '文件夹创建成功'
			os.mkdir(folder_name)
			return True
		else:
			print '文件夹已存在'
			return False

	# 写入信息
	def write_to_file(self,content):
		f = open('movie/test.txt','w')
		f.write(content)
		f.close()


	def start(self):
		self.mkdir()
		f = open('movie/msg.txt','w')
		for i in range(0,10):
			url = self.url+'?offset='+str(i*10)
			# print url
			lists = self.parse_one_page(url)
			for item in lists:
				print item[0],item[2],item[3].strip(),item[4].strip(),item[5],item[6],item[1]
				msg = '排名：%s, 名字:[%s], %s, 评分：%s \n' % (item[0],item[2],item[4].strip(),item[5]+item[6])
				f.write(msg)
		f.close()
		
# 爬取猫眼电影Top100,每页10条，总共10页,参数为offset
spider = Spider()
spider.start()


















