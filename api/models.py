from django.db import models
from datetime import timedelta, datetime
from django.contrib.auth.models import User
# Create your models here.


class UserDetail(models.Model):
    user = models.ForeignKey(User)
    user_type = models.IntegerField(blank=False, default=0) # 사용자 타입 (0:관리자 / 1:광고주 / 2: 크리에이터)
    create_date = models.DateTimeField() # 가입 시간
    last_date = models.DateTimeField(blank=True)
    token = models.CharField(max_length=100, blank=True)
    
    def save(self, *args, **kwargs):
        if self.user:
            now_time = datetime.now()
            expire_second = 3600

            self.create_date = now_time + timedelta(seconds = expire_second)
            
        super(UserDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email


class Ads(models.Model):
    ad_type = models.CharField(max_length = 100)
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(UserDetail)
    budget = models.IntegerField(blank=False, default=0)
    limit = models.IntegerField(blank=False, default=0)
    create_at = models.DateTimeField(auto_now=False)

    def save(self, *args, **kwargs):
        if self.ad_type:
            now_time = datetime.now()
            expire_second = 3600

            self.create_at = now_time + timedelta(seconds = expire_second)
            
        super(Ads, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class AdRequest(models.Model):
    ad_id = models.ForeignKey(Ads)
    sender = models.ForeignKey(UserDetail)
    #recipient = models.ForeignKey(UserDetail)
    accept = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return self.name


class Board(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(UserDetail)
    contents = models.TextField()
    create_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Reply(models.Model):
    board_id = models.ForeignKey(Board)
    contents = models.CharField(max_length=300)
    author = models.ForeignKey(UserDetail)
    create_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name