# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render

def index(request):
	latest_added_items = Poll.objects.all().order_by('-create_at')[:10]
	context = {'latest_added_items': latest_added_items}
	return render(request, 'feedin/index.html', context)



