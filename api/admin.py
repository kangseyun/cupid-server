from django.contrib import admin
from api.models import UserDetail, Ads, AdRequest, Board, Reply

# Register your models here.


admin.site.register(UserDetail)
admin.site.register(Ads)
admin.site.register(AdRequest)
admin.site.register(Board)
admin.site.register(Reply)
