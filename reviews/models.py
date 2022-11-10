from django.db import models
from django.conf import settings

# Create your models here.

class Review(models.Model):
    star_list = [
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), # 
    ] # 문자열은 따옴표 필요하며, 선택 범위를 지정해줌(앞에 것은 출력할때 보여주는 별, 뒤에것은 입력할때 보여주는 별)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 한명의 유저가 여러개의 리뷰를 작성할 수 있음(외래키)
    star = models.CharField(max_length=5, choices=star_list)
    content = models.TextField()