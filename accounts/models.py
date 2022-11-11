from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # get_user_model()은 user모델을 커스텀한 경우 get_user_model()을 사용
    is_seller = models.BooleanField(default=False) # 참/거짓 모델, False = 구매자, True = 판매자로 하여 역할 부여