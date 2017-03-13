'''
Created on 2017-03-10

@author: chaohu
'''

from django.conf.urls import url
from wm_app import views

urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name="detail")
]