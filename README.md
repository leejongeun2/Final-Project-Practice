## 📗Semi Project02(Practice)

---

`프로젝트에 참여하지 않고 , 개인공부 시간을 통해 Django 와 Front-end학습(with 종은, 주현)`

---

## 11.09

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

```python
# url.py
# 현재 같은 경로에 있는 views파일 참조
from . import views
```

```python
# views.py

def index(request):
    return render(request, "products/index.html") # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌
```

### static

`static`

- STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  
  - 로고와 같이 고정적으로 삽입하는 정적 이미지

`STATIC_URL = '/static/'`

- 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로

`STATICFILES_DIRS = [BASE_DIR / 'static']`

- 이곳에 지정한 경로에 모든 파일을 모은다.

### image

`MEDIA_ROOT = BASE_DIR / 'images'`

- 업로드가 끝난 파일을 배치할 최상위 경로를 지정하는 설정 항목

`MEDIA_URL = '/media/'`

- 웹 페이지에서 사용할 이미지 파일의 최상위 URL 경로

`DEFAULT_AUTO_FIELD ='django.db.models.BigAutoField'`

- 64비트보다 더 큰 정수값을 사용하고 싶을 때 모델에 각 정의해주는 것보다 여기서 전역에 적용되도록 기재함 ,Django에서 자동 생성

`AUTH_USER_MODEL = "accounts.User"`

- User를 나타내는데 사용하는 모델을 accounts 앱의 커스터마이징한 user모델임을 정의해줌

## 11.10

## Model

`ManyTomanyField`

- Source Model이 Target Model에게 어떤 행동을 통해, 새로운 테이블에 값을 추가 할 때 

```py
# Source Model = Patient, Target Model = Doctor
# ManyToManyField = doctors (Doctor, related_name = 'patients')

patient1.doctors.all()
# 환자1이 예약한 의사 모두 확인


patient1.doctors.add(doctor1)
# 환자1이 의사1에게 예약


# doctor1이 patient2을 예약
doctor1.patient_set.add(patient2)
# doctor1이 patient2을 예약(역참조)
# related_name = patients 
# patients = patient_set ⭐️
```

```python
doctor1 = Doctor.objects.get(pk=1)


# 1번 의사 조회하기

doctor1.patients.all()
# 의사1이 예약한 환자목록 확인 => 역참조
# related_name = patients 
# patients = patient_set ⭐️
```

```python
# 기존 Reservation 탐색 후 제거 대신 .remove() 사용

doctor1.patient_set.remove(patient1)
# 닥터1이 환자1 예약취소

doctor1.patient_set.all()
# 닥터1의 환자 모두 확인
# 환자 2번만 조회된다.

patient1.doctors.all()
# 환자1이 예약한 의사 모두 조회
# 의사 1을 삭제하여 조회되지 않는다.
```

```python
patient2.doctors.remove(doctor1)
#환자2가 닥터1의 진료 취소

patient2.doctors.all() 
# 환자 2가 예약한 의사 모두 확인 (닥터1을 취소하여 조회되지 않는다.)

doctor1.patient_set.all()
# 닥터 1이 예약한 환자 모두 확인( 조회되지 않는다.)
```

## 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없음

- Django의 ManyToManyField는 중개 테이블을 자동으로 생성

- Django의 ManyToManyField는 M:N 관계를 가진 모델 어디에 위치해도 상관없음
  <<<<<<< HEAD
  
  - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

- related_name
  
  - target model이 source model을 참조할 때 사용할 manager name

- symmetrical
  
  - True : 내가 당신의 친구라면 당신도 내 친구

=======

- 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

- related_name
  
  - target model이 source model을 참조할 때 사용할 manager name

- symmetrical
  
  - True : 내가 당신의 친구라면 당신도 내 친구

- False : 친구 아님, 즉 대칭을 이루지 않는다.

## 👏Figma를 이용한 구상

>  Figma를 이용하여 제작할 홈페이지의 프론트를 구상하였다.

- 디자인 구상
  
  - ZIGZAG 라는 여성 쇼핑몰 사이트를 참고하였다.

[![지그재그](https://i.esdrop.com/d/f/teJqrUQey5/y8PLFjj2vB.png)](https://zigzag.kr/)

`ZIGZAG 의 특성`

- 주로 핑크색과 검정색으로 디자인됨

- 역동적인 프론트 디자인

- 굵직굵직하고 감각적인 폰트



`Project ZUGZOG`

>  지그재그를 근간으로 하여 디자인을 시도하였다.

`nav-bar`

![navbar](https://i.esdrop.com/d/f/teJqrUQey5/muOg1gaXQH.png)

`main page`

![](https://i.esdrop.com/d/f/teJqrUQey5/1SsO26Kuzc.png)

`detail page`

![](C:\Users\이주현\AppData\Roaming\marktext\images\2022-11-11-21-52-07-image.png)



`Form`

- 현재 로그인,리뷰등록,수정Form 활용 계획

![](https://i.esdrop.com/d/f/teJqrUQey5/YrY7dHjP9z.png)

`Review`, `Profile`

![](https://i.esdrop.com/d/f/teJqrUQey5/cIA2qNFIvs.png)

 `Like`

![](https://i.esdrop.com/d/f/teJqrUQey5/wPyKAuY9bT.png)

- 추후 변동사항이 있으면 추가할 계획

- 디자인 규격을 통일하지 않아 조금 어긋나거나 난잡한 부분이 있다... 수정 계획

- FIGMA는 매우 유용한 툴임에 틀림없다.

- 이후 FIGMA 사용에선 Section 구역 기획을 통한 완벽한 대칭과 간격을 시도해 볼 예정



## 11.11



### Keword

`pip uninstall -r requirements.txt -y`

- 패키지로 설치 된 것을 한번에 지우는 명령어



`오류 : cannot assign simplelazyobject`

- 로그인 상태에서 해야 할 일을 비로그인 상태로 진행하기 때문에 생기는 오류이다.

- 우리가 쓴 request.user는 로그인 전에는 AnonymousUser가 매핑되고 로그인 이후에 User객체가 맵핑된다.

- 따라서 하고자 하는 일을 수행하기 전에 로그인을 하면 오류가 안 뜬다.로그인이 필요하도록 @login_required를 사용하면 오류가 뜨는 것을 해결할 수 있다.


`{% url 'app name:url name' %}`

* 버튼 클릭하여 url로 이동 시,



`BooleanField`

- 참/거짓 모델, False = 구매자, True = 판매자로 하여 역할 부여



`{% if request.resolver_match.url_name == 'create' %}`

- resolver_match = 어떤 url을 통해서 왔는지 검사하는 인스턴스

- 따라서 create url로 왔는지 여부를 검사



`{{ product.user }} ? {{ product.user.username }}?`

- user 필드의 모델은 user모델이고, 그 모델에 username이 있어서 username 보여짐

- 둘 다 같은 결과



`like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,` 

`related_name = 'like_product')`

- 한 상품은 사용자에게 좋아요를 여러개 받을 수 있고,

- 한 사람도 여러 상품에 좋아요를 할 수 있다.



### views.py

```python
# accounts/views.py
def signup(request):
    if request.method == 'POST': # 요청 받아서 제출 누르면
        form = CustomUserCreationForm(request.POST) # 커스텀 폼에 요
#청 받은 것이 담기고 그것을 폼이란 변수에 저장
        if form.is_valid(): # 유효하다면 
            form.save() # 저장하고 
            return redirect('products:index') # url로 이동
    else:
        form = CustomUserCreationForm() # post 요청이 아니면
                            #(제출 버튼을 안누르면) 빈 폼을 보여줌

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context) # 유효하지 
# 않을 때(post일때), 사용자의 인풋을 다 받아서, 검증까지 해서 
#에러메시지를 저장한 product_form(템플릿 내에서 부트스트랩 폼에 사용)
    # 해당 페이지 접속일 (글생성 x)때는 else의 product_form이 들어감


def login(request):
    if request.method == 'POST': # 로그인 버튼 누르면
        form = AuthenticationForm(request, data=request.POST) # request를
 # 첫번째 인자로 취함, 유효성 검사를 위해 "data=" 을 통해 판별, 유저가 존재하는지 
# 검증하는 모델폼
        if form.is_valid(): # 유효하면 
            auth_login(request, form.get_user()) # auth_login 함수는 
# 세션에 유저를 기록하는 함수, AuthenticationForm의 인스턴스 메서드, 
# 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
            # return redirect(request.GET.get('next') or 'products:index') 
            # http://localhost:8000/accounts/login/?    next = /products/1/update/
            if request.GET.get('next'): # next라면
                return redirect(request.GET.get('next')) # 원래 next 
                                                        # url로 가고
            else: # next가 아니라면
                return redirect('products:index') # 정상 로그인이니까 로그인 후 index로 이동을 하기

    else:
        form = AuthenticationForm(request) # 로그인 버튼을 누르지 않으면

    context = {
        'form': form 
    }

    return render(request, 'accounts/login.html', context) # 유효성 검사에
# 실패하거나, 로그인 페이지 접속만 한 경우, 담긴 값을 가지고 
# 다시 로그인 페이지로 이동


@login_required
def logout(request):
    auth_logout(request) # 요청 유저에 대한 세션 정보를 삭제함, 
                        # HttpRequest 객체를 인자로 받고 반환 값이 없음
    return redirect('products:index')
```

```python
# products.py

def index(request):
    
    products = Product.objects.all() # Product 모델의 객체를 다 가져옴 
    context = {
        'products':products,
    }
    return render(request, "products/index.html", context) # 템플릿 네임 
                                # 적어주고, 이쪽으로 context 값을 넘겨줌


def create(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES) # 사용자가
                # 요청하여 Productform에 담긴 포스트를 productform 변수에 저장

        if product_form.is_valid():
            product = product_form.save(commit=False) # 저장하기 전에 잠깐 
                                            # 멈추기 위해 commit=false사용
            product.user = request.user # product.user와 요청한 
                                        # user가 같다를 정의 
            product.save() # 위에 요청 받은 폼을 저장, 
          # 값을 만들고 저장하는 용도고 값을 보내줄 것이 없으니까 redirect를 사용
            return redirect('products:index') # url로 이동시켜줄 뿐
                    # (app name:url name) 글작성 후 제출하면 index로 이동
    else: 
        product_form = ProductForm() # post 요청이 아니면
                                     # (제출 버튼을 안누르면) 빈 폼을 보여줌

    context = {
        "product_form": product_form # 유효하지 않을 때, 
# 사용자의 인풋을 다 받아서, 검증까지 해서 에러메시지를 저장한 
#product_form(템플릿 내에서 부트스트랩 폼에 사용)
        # post일 때는 post의 product_form이 여기에 해당 되고, 
# 해당 페이지 접속일 (글생성 x)때는 else의 product_form이 들어감
    }

    return render(request, "products/form.html", context) # 제출에 
                                # 이슈가 있다면 값을 보내며 다시 폼으로 돌아가기


def detail(request, product_pk): # 요청 받은 것에 product_pk가 포함됨
    product = Product.objects.get(id=product_pk) # id가 요청받은 product_pk가 같은 것을 가져옴

    context = {
        "product":product 
    }

    return render(request, "products/detail.html", context) # 요청 받은 
                                      # 것을 가지고, detail 페이지에 값을 전달


def update(request, product_pk): # url에 product_pk 받아야하므로 요청 받은 것에 product_pk 가포함됨
    product = Product.objects.get(id=product_pk) # id가 요청받은 product_pk가 같은 것을 가져옴

    if request.method == "POST": # 업데이트 제출 버튼 눌렀을 때
        product_form = ProductForm(request.POST, request.FILES, instance=product) #  기존에 모델에 있는 것을 넣어 놓은 것과 요청된 포스트와 요청 된 파일을 불러옴

        if product_form.is_valid(): # 위 폼이 유효하다면
            product_form.save() # 저장

            return redirect("products:detail", product_pk) # 몇번 상품의 
                                                # 디테일 페이지에 보내줄껀지? 
    else:
        product_form = ProductForm(instance=product) # 기존 모델에 저장 
                                                    # 되어있는 값을 보여줌

    context = {
        "product_form": product_form # 유효하지 않을 때는 요청 받은 
                               # product_form, 제출 안눌렀을 때는 바로위의 폼
    }

    return render(request, "products/forms.html", context) # 유효하지 
   # 않을 때나, 제출 안눌렀을 때는 위의 컨텍스트 값을 가져와서 forms.html을 보여줌
```

## 11.13

### Keyword

`return 과 redirect 구분`

- render 는 템플릿을 불러오고

- redirect 는 URL로 이동

- URL 로 이동한다는 건 그 URL 에 맞는 views 가 다시 실행될테고 여기서 render 를 할지 다시 redirect 할지 결정

`@login_required`

- @안하면 접속이 가능하게 됨, 그러므로 @로 로그인화면이 보여지도록 해야함

`{% if request.user.is_authenticated %}`

- request.user는 뒤에나오는 것을 요청하는 사람

`request.user.id`

- 판매자가 되려는 식별할 수 있는 번호 id가 있어야 되기 때문에 pk 값을 불러 와 준다

`역참조에서...`

- _set 은 related_name 으로 대체 가능하다

- set은 1: N 관계에서 , related_name은 N:M 관계에서 주로 쓰인다.

- source Model, Target Model 을 잘 구분하여 사용하여야 한다

```python
# doctor1이 patient2을 예약
doctor1.patient_set.add(patient2)
# doctor1이 patient2을 예약(역참조)
# related_name = patients 
# patients = patient_set ⭐️
```

```python
# products/views.py

jjim = get_user_model().objects.get(id=user_pk).jjim_product.all()

# related_name = jjim_product 라고 모델에서 이미 정의
# abstractuser에서 지정한 User값을 사용하기 위해 get_user_model() 사용
```

### views.py

```python
# accounts.py
@login_required
def register_seller(request, user_pk): # 몇번 사용자가 true가 될것인지 알아야 하니까 user_pk값을 넣어줌
    user = get_user_model().objects.get(id=user_pk) # id가 요청 받은 user_pk인 것을 가져옴
    user.is_seller = True       # seller = True, customer = False
    user.save()                 

    return redirect('products:index')   
```

```python
# products.py


def add_jjim(request, product_pk): # product_pk값을 불러와야 되는 이유는 해당 상품을 장바구니에 넣는 것이니까 
    product = Product.objects.get(id=product_pk) # 특정 상품 가져오고

    if request.user in product.jjim.all(): # 상품에 찜이 되어있는 모든 것 중 요청유저가 있다면
        product.jjim.remove(request.user) # 상품이 요청유저의 찜을 지움
    else: # 누른적이 없는 경우, 
        product.jjim.add(request.user) # 상품이 요청유저에게 찜을 받는다. 

    return redirect('products:detail', product_pk) # detail로 보낼 때는 상품에 대한 
                                        # pk가 필요하니까 product_pk를 써줌


def show_jjim(request, user_pk):
    jjim = get_user_model().objects.get(id=user_pk)# 특정 유저 데이터를 가지고 오고 
    jjim1 = jjim.jjim_product.all() # 모델.related_name.method()
    # 특정 유저가(user_pk)가 찜한 상품 목록 모두 확인
    context = {
        'jjim': jjim1
    }

    return render(request, 'products/jjim.html', context) # 값을 던져준 html을 보여줌
```

## 11.14
* 리뷰 user_id에 저장되어야 할 작성자 정보가 누락되었기 때문