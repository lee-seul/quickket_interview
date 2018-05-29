# coding: utf-8


from django.conf.urls import url

from github_api import views


urlpatterns = [
    url(r'^events$', views.github_events, name='github_events'),
]
