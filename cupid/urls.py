from django.conf.urls import url, include
from django.contrib import admin
from api.views.auth import login, join, logout
from api.views.ad import ad, ad_detail, ad_write, ad_count, ad_write
from api.views.home import index, my, notification, chat, ad_status, trade

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^api/v1/auth/join/$', join, name='join'),
    url(r'^api/v1/auth/logout/$', logout, name='logout'),
    url(r'^api/v1/ad/$', ad),
    url(r'^api/v1/ad/(?P<id>\d+)/$', ad_detail, name='ad_detail'),   
    url(r'^api/v1/ad/count/$', ad_count),   
    url(r'^my/$', my, name='my'),  
    url(r'^my/chat/$', chat, name='chat'),   
    url(r'^my/notification/$', notification, name='notification'),   
    url(r'^my/ad_write/$', ad_write, name='ad_write'),   
    url(r'^my/ad_status/$', ad_status, name='ad_status'),   
    url(r'^my/trade/$', trade, name='trade'),   

]
