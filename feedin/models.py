# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Tag(models.Model):
	tag = models.CharField(max_length=100)

	def __unicode__(self):
		return self.tag

class Commodity(models.Model):
	# 商品连接
	url = models.CharField(max_length=255)
	# 商品标题
	title = models.CharField(max_length=255)
	# 原价
	price = models.DecimalField(max_digits=12, decimal_places=2)
	# 促销价
	discount_price = models.DecimalField(max_digits=12, decimal_places=2)
	# 图片地址 
	imgurl = models.CharField(max_length=255)
	# 三十天销售量
	seles = models.IntegerField(default=0)
	# 评价星级
	appraisal = models.IntegerField(default=0)

	tags = models.ManyToManyField(Tag)
	
	create_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

