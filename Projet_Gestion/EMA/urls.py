from django.conf.urls import patterns, url
from EMA import views


urlpatterns = patterns('',
        url(r'', views.index, name='index'))