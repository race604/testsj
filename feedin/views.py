# -*- coding: utf-8 -*-

# Create your views here.

import urllib
import sgmllib
import re
from HTMLParser import HTMLParser
from django.shortcuts import render

from feedin.models import Commodity

#class HtmlTagParse(HTMLParser):

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

def index(request):
	latest_added_items = Commodity.objects.all().order_by('-create_at')[:10]
	context = {'latest_added_items': latest_added_items}
	return render(request, 'feedin/index.html', context)

def add(request):
	return render(request, 'feedin/add.html')
	
def parse(request):
	try:
		url = request.post['url']
		item = Commodity(url=url)
		page = urllib.urlopen(url)

	return render(request, 'feedin/add.html')

