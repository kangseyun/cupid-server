from django.db import models
from datetime import timedelta, datetime
# Create your models here.


class UserDetail(models.Model):
    email = models.CharField(max_length = 50) # email
    password = models.CharField(max_length = 20)  # 사용자 비밀번호
    name = models.CharField(max_length = 20)    # 사용자 이름
    user_type = models.IntegerField(blank=False, default=0)             # 사용자 타입 (0:관리자 / 1:광고주 / 2: 크리에이터)
    create_date = models.DateTimeField()         # 가입 시간
    
    def save(self, *args, **kwargs):
        if self.email:
            now_time = datetime.now()
            expire_second = 3600

            self.create_date = now_time + timedelta(seconds = expire_second)
            
        super(UserDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Ads(models.Model):
    ad_type = models.CharField(max_length = 100)
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(UserDetail)
    budget = models.IntegerField(blank=False, default=0)
    limit = models.IntegerField(blank=False, default=0)
    create_at = models.DateTimeField(auto_now=False)

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