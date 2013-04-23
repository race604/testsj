# -*- coding: utf-8 -*-
import re
from HTMLParser import HTMLParser
from feedin.models import Commodity

def getValueFromTag(html):
	p = re.compile(r'<[^>]+>')
	return p.sub('', html)

def getAttribute(html, attr):
	attr = attr + '='
	start = html.find(attr)
	if start >= 0:
		start += len(attr)+1
		end = html.find(html[start-1], start)
		return html[start:end]

def findFloat(data):
	p = re.compile('[\d.]+')
	m = p.search(data)
	return float(m.group())


class TaobaoParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.item = Commodity()
		self.state = 0
		
	def handle_starttag(self, tag, attrs):
		# 开始处理
		if self.state == 0:
			if tag == 'div':
				for attr in attrs:
					if attr[0] == 'id' and attr[1] == 'detail':
						self.state = 1
		# 标题
		elif self.state == 1:
			if tag == 'h3':
				self.state = 2
		# 图片 
		elif self.state == 2:
			if tag == 'ul':
				for attr in attrs:
					if attr[0] == 'id' and attr[1] == 'J_UlThumb':
						self.state = 3
		elif self.state == 3:
			if tag == 'img':
				for attr in attrs:
					if attr[0] == 'src':
						self.item.imgurl = attr[1]
						self.state = 4
		# 原价
		elif self.state == 4:
			if tag == 'em':
				for attr in attrs:
					if attr[0] == 'class' and attr[1] == 'tb-rmb-num':
						self.state = 5
		elif self.state == 5:
			if tag == 'strong':
				for attr in attrs:
					if attr[0] == 'class' and attr[1] == 'tb-rmb-num':
						self.state = 6
		elif self.state == 6:
			if tag == 'em':
				for attr in attrs:
					if attr[0] == 'class' and attr[1] == 'J_TDealCount':
						self.state = 7
		elif self.state == 7:
			if tag == 'em':
				for attr in attrs:
					if attr[0] == 'id' and attr[1] == 'J_RateStar':
						self.state = 8

	def handle_data(data):
		if self.state == 2:
			self.item.title += data
		elif self.state == 3:
			self.item.price = Decimal(data)
		elif self.state == 4:
			self.item.discount_price = Decimal(data.rstrip('"'))
		elif self.state == 5:
			self.item.sales = int(data)
		elif self.state == 6:
			self.item.rate = findFloat(data)
		
			
