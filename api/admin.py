from django.contrib import admin
from api.models import UserDetail, Ads, AdRequest, Reply, Ad_type, Category


admin.site.register(UserDetail)
admin.site.register(Ads)
admin.site.register(AdRequest)
admin.site.register(Reply)
admin.site.register(Category)
admin.site.register(Ad_type)
