from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    # 리뷰
    path("<int:product_pk>/", views.index, name="index"), # 리뷰 목록 리스트
    path("<int:product_pk>/create/", views.create, name="create"), # 상품 리뷰 작성
    path("<int:review_pk>/update/", views.update, name="update"), # 상품 리뷰 수정
    path("<int:review_pk>/delete/", views.delete, name="delete"), # 상품 리뷰 삭제
]
