from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'*', include(ask.qa.views.test), name='test'),
]