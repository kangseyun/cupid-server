from django.conf.urls import url, include
from django.contrib import admin
from api.views.auth import login, join, logout
from api.views.resume import resume, resume_detail, resume_regi, resume_regi_delete
from api.views.ad import ad, ad_detail, ad_write, ad_count, ad_write, ad_result, trade_accept
from api.views.home import index, my, notification, chat, ad_status, trade
from api.views.ad import trade as trade_request


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^api/v1/auth/join/$', join, name='join'),
    url(r'^api/v1/auth/logout/$', logout, name='logout'),
    url(r'^api/v1/resume/$', resume),
    url(r'^api/v1/resume/detail/(?P<id>\d+)/$', resume_detail, name='resume_detail'),
    url(r'^api/v1/ad/$', ad),
    url(r'^api/v1/ad/(?P<id>\d+)/$', ad_detail, name='ad_detail'),
    url(r'^api/v1/ad/result/$', ad_result, name='ad_result'),
    url(r'^api/v1/ad/count/$', ad_count),   
    url(r'^my/$', my, name='my'),  
    url(r'^my/chat/$', chat, name='chat'),   
    url(r'^my/notification/$', notification, name='notification'),   
    url(r'^my/ad_write/$', ad_write, name='ad_write'),   
    url(r'^my/ad_status/$', ad_status, name='ad_status'),   
    url(r'^my/trade/$', trade, name='trade'),   
    url(r'^trade/request/$', trade_request , name='trade_request'),   
    url(r'^trade/accept/$', trade_accept , name='trade_accept'),   
    url(r'^resume/regi/$', resume_regi , name='resume_regi'),   
    url(r'^resume/regi/delete/$', resume_regi_delete, name='resume_regi_delete'),   
    url(r'^ad/result/$', trade_request , name='ad_result'),   
]
