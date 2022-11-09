# 📗Semi Project02(Practice)
## 11.09
---

`프로젝트에 참여하지 않고 , 개인공부 시간을 통해 Django 와 Front-end학습(with 종은, 주현)`

---
`ERD 그리는 법`
* https://app.diagrams.net/ 프로그램 사용하여, 모델 간 관계 정의
* 마우스 커서를 놓을 때, 화살표가 나오고 화살표 클릭 시 필드 생성
* 마우스 커서를 필드 바깥쪽에 넣을 때 녹색 점 노출, 점을 끌어당겨서 다른 모델 필드의 바깥쪽 녹색점에 연결하면 정확하고 깔끔하게 가운데로 연결 됨 
* 오른쪽 선 스타일에서 꺾이는 선을 선택해야 선이 꺾여서 노출 

`STATICFILES_DIRS`

* 개발 단계에서 사용하는 정적 파일이 위치한 경로들을 지정하는 설정 항목
  

`CASCADE`

* 연결된 부분을 지우면 다 같이 지워지는 기능
  

ex ) 글을 지우면 리뷰까지 다 삭제되게 구현하고 싶을 때,

`Nullable Type?`

* Null을 가질 수 없는 데이터 타입을 Null을 가질 수 있는 타입으로 만든 새로운 타입

`url.py`
```python```

## 현재 같은 경로에 있는 views파일 참조
* from . import views 

`views.py`
```python
def index(request):
    return render(request, "products/index.html") # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌

# static
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # 로고와 같이 고정적으로 삽입하는 정적 이미지, 
STATIC_URL = '/static/' # 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
STATICFILES_DIRS = [BASE_DIR / 'static'] # 이곳에 지정한 경로에 모든 파일을 모은다.


# image
MEDIA_ROOT = BASE_DIR / 'images' # 업로드가 끝난 파일을 배치할 최상위 경로를 지정하는 설정 항목
MEDIA_URL = '/media/' # 웹 페이지에서 사용할 이미지 파일의 최상위 URL 경로

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # 64비트보다 더 큰 정수값을 사용하고 싶을 때 모델에 각 정의해주는 것보다 여기서 전역에 적용되도록 기재함 ,Django에서 자동 생성

AUTH_USER_MODEL = "accounts.User" #  User를 나타내는데 사용하는 모델을 accounts 앱의 커스터마이징한 user모델임을 정의해줌




 