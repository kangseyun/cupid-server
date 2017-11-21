from django.conf.urls import url, include
from django.contrib import admin
from api.views.auth import login, join, logout
from api.views.ad import ad, ad_detail, ad_write, ad_count
from api.views.home import index, my

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^api/v1/auth/join/$', join, name='join'),
    url(r'^api/v1/auth/logout/$', logout, name='logout'),
    url(r'^api/v1/ad/$', ad),
    url(r'^api/v1/ad/write/$', ad_write),
    url(r'^api/v1/ad/(?P<id>\d+)/$', ad_detail),   
    url(r'^api/v1/ad/count/$', ad_count),   
    url(r'^my/$', my, name='my'),   
]
