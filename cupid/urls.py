from django.conf.urls import url, include
from django.contrib import admin

from api.views.auth import login, join
from api.views.ad import ad, ad_detail


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login),
    url(r'^join/$', join),
    url(r'^ad/$', ad),
    url(r'^ad/write$', ad),
    url(r'^ad/(?P<id>\d+)/$', ad_detail),    
]
