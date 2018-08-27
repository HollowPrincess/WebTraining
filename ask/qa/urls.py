from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('qa.urls')), #URL / 
    url(r'^login/', include('qa.urls')), #URL /login/
    url(r'^signup/', include('qa.urls')), #URL /signup/
    url(r'^question/(?P<ID>[0-9])+/', include('qa.urls')), #URL /question/<ID>
    url(r'^ask/', include('qa.urls')), #URL /ask/
    url(r'^popular/', include('qa.urls')), #URL /popular/
    url(r'^new/', include('qa.urls')), #URL /new/   
]

