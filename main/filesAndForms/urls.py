from django.conf.urls import patterns, url
from filesAndForms import views

urlpatterns = patterns('',
	url(r'^list/$', views.list, name='list'),)
