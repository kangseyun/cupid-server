from django.contrib import admin
from api.models import UserDetail, Ads, AdRequest, Reply, Category, Location
from api.models import Notification, NotificationType, AdTrade, Recommend, Resume, ADResult


admin.site.register(UserDetail)
admin.site.register(Ads)
admin.site.register(AdRequest)
admin.site.register(Reply)
admin.site.register(Resume)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Notification)
admin.site.register(NotificationType)
admin.site.register(AdTrade)
admin.site.register(Recommend)
admin.site.register(ADResult)



