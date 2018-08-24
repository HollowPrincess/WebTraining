"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('qa.urls')), #URL / 
    url(r'^login/$', include('qa.urls')), #URL /login/
    url(r'^signup/$', include('qa.urls')), #URL /signup/
    url(r'^question/<(?P<ID>[0-9])+>/$', include('qa.urls')), #URL /question/<ID>
    url(r'^ask/$', include('qa.urls')), #URL /ask/
    url(r'^popular/$', include('qa.urls')), #URL /popular/
    url(r'^new/$', include('qa.urls')), #URL /new/
    url(r'^admin/', include(admin.site.urls)),
]
