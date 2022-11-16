from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'products'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"), # 상품 글 작성
    path("<int:product_pk>/", views.detail, name="detail"), # 상품 조회 페이지
    path("<int:product_pk>/update/", views.update, name="update"), # 상품 글 수정
    path("<int:product_pk>/delete/", views.delete, name="delete"), # 상품 글 삭제
    path("<int:product_pk>/add_jjim/", views.add_jjim, name="add_jjim"), # 찜 상품 담기
    path("show_jjim/<int:user_pk>/", views.show_jjim, name="show_jjim"), # 찜 조회
    path("delete_jjim/<int:product_pk>", views.delete_jjim, name="delete_jjim"), # 장바구니 상품 삭제
    path('<int:product_pk>/like/', views.like, name="like"), # 좋아요
]