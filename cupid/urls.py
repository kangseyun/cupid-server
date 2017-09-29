from django.conf.urls import url, include
from django.contrib import admin

from api.views.auth import login, join
from api.views.ad import ad, ad_detail, ad_write, ad_count


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/auth/admin/', admin.site.urls),
    url(r'^api/v1/auth/login/$', login),
    url(r'^api/v1/auth/join/$', join),
    url(r'^api/v1/ad/$', ad),
    url(r'^api/v1/ad/write/$', ad_write),
    url(r'^api/v1/ad/(?P<id>\d+)/$', ad_detail),   
    url(r'^api/v1/ad/count/$', ad_count),   
]
