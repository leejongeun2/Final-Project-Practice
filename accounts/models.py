from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_seller = models.BooleanField(default=False) # 참/거짓 모델, False = 구매자, True = 판매자로 하여 역할 부여