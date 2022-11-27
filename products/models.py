from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from reviews.models import Review

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(640, 480)],
                                format='JPEG',
                                options={'quality':90})
    content = models.TextField()
    jjim = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'jjim_product') # 한 상품은 여러명의 사용자에게 찜을 받을 수있고, 사용자는 여러 상품에 찜을 할 수 있다.
    review = models.ManyToManyField(Review, related_name = 'review_product') #  한 상품은 여러 리뷰가 있을 수 있고, 한 리뷰는 여러 상품에 있을 수 있다.   
    # 특정 상품에 작성된 리뷰는 여러개 있을 수 있고, 특정 리뷰가 쓰여진 상품들은 여러개 있을 수 있다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_products')
    # 한 상품은 여러 사람들한테 좋아요를 받을 수 있고, 한사람은 여러 상품에 좋아요를 할 수 있다.

class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.TextField()
    image_url = models.TextField()
