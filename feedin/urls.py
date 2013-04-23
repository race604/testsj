from django.conf.urls import patterns, url

from feedin import views

urlpatterns = patterns('',
		url(r'^$', 'feedin.views.index', name='index'),
		url(r'^add/$', 'feedin.views.add', name='add'),
		)
