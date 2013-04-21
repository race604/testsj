from django.conf.urls import patterns, url

from feedin import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index')
		url(r'^add/$', views.index, name='add')
		)
