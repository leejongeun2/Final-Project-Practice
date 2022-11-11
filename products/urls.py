from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'products'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"), # 상품 글 작성
    path("<int:product_pk>/", views.detail, name="detail"), # 상품 조회 페이지
    path("<int:product_pk>/update/", views.update, name="update"), # 상품 글 수정
]