from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class User(AbstractUser): # get_user_model()은 user모델을 커스텀한 경우 get_user_model()을 사용
    is_seller = models.BooleanField(default=False) # 참/거짓 모델, False = 구매자, True = 판매자로 하여 역할 부여

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )