from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Product(models.model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(640, 480)],
                                format='JPEG',
                                options={'quality':90})
                    # 1. 모델 재정의 2.썸네일
    content = models.TextField()
    # cart = 
    # review = 
    # like_uesrs = 