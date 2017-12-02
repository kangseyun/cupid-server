from django.db import models
from datetime import timedelta, datetime
from django.contrib.auth.models import User
# Create your models here.


class UserDetail(models.Model):
    user = models.ForeignKey(User)
    user_type = models.IntegerField(blank=False, default=0, verbose_name='유저 타입') # 사용자 타입 (0:관리자 / 1:광고주 / 2: 크리에이터)
    token = models.CharField(max_length=100, blank=True, verbose_name='토큰')
    tel = models.CharField(max_length=15, verbose_name='번호', blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(UserDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email


class NotificationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        super(NotificationType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserDetail)
    type = models.ForeignKey(NotificationType)
    content = models.CharField(max_length=100)
    check = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Notification, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class Category(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='이름')

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Resume(models.Model):
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Resume, self).save(*args, **kwargs)


class Ads(models.Model):    
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, verbose_name='광고타입')
    title = models.CharField(max_length=50, verbose_name='제목')
    author = models.ForeignKey(UserDetail, verbose_name='작성자')
    budget = models.IntegerField(blank=False, default=0)
    limit = models.IntegerField(blank=False, default=0)
    create_at = models.DateTimeField(auto_now=False)

    def save(self, *args, **kwargs):
        if self.title:
            now_time = datetime.now()
            expire_second = 3600
            self.create_at = now_time + timedelta(seconds = expire_second)
            
        super(Ads, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class AdTrade(models.Model):
    id = models.AutoField(primary_key=True)
    creater = models.ForeignKey(UserDetail, verbose_name='크리에이터', related_name='create')
    adbos = models.ForeignKey(UserDetail, verbose_name='광고주', related_name='ad')
    status = models.IntegerField(default = 0) # 0 진행중 1 완료
    ad = models.ForeignKey(Ads)
    create_at = models.DateTimeField(auto_now=False)

    def save(self, *args, **kwargs):
        if self.id:
            now_time = datetime.now()
            expire_second = 3600
            self.create_at = now_time + timedelta(seconds = expire_second)
            
        super(AdTrade, self).save(*args, **kwargs)


class AdRequest(models.Model):
    ad_id = models.ForeignKey(Ads)
    sender = models.ForeignKey(UserDetail)
    #recipient = models.ForeignKey(UserDetail)
    accept = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return self.name


class Board(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    author = models.ForeignKey(UserDetail, verbose_name='작성자')
    contents = models.TextField(verbose_name='내용')
    create_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Reply(models.Model):
    board_id = models.ForeignKey(Board, verbose_name='부모 게시물')
    contents = models.CharField(max_length=300, verbose_name='내용')
    author = models.ForeignKey(UserDetail, verbose_name='작성자')
    create_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name


class TontataChat(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=300, verbose_name='내용')
    from_user = models.ForeignKey(UserDetail, related_name='from_user')
    to_user = models.ForeignKey(UserDetail, related_name='to_user')
    create_at = models.DateTimeField(auto_now=True)
    check = models.BooleanField(default=False)