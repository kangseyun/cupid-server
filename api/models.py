from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.CharField(max_length = 20)  # 사용자 아이디
    pw = models.CharField(max_length = 20)  # 사용자 비밀번호
    name = models.CharField(max_length = 20)    # 사용자 이름
    user_type = models.IntegerField             # 사용자 타입 (0:관리자 / 1:광고주 / 2: 크리에이터)
    create_date = models.DateTimeField()         # 가입 시간
