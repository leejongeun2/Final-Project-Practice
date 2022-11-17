from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def index(request):
    products = Product.objects.all() # Product 모델의 객체를 다 가져옴 
    context = {
        'products':products,
    }
    return render(request, "products/index.html", context) # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌
    

def create(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES) # 사용자가 요청하여 Productform에 담긴 포스트를 productform 변수에 저장

        if product_form.is_valid():
            product = product_form.save(commit=False) # 저장하기 전에 잠깐 멈추기 위해 commit=false사용
            product.user = request.user # product.user와 요청한 user가 같다를 정의 
            product.save() # 위에 요청 받은 폼을 저장, 값을 만들고 저장하는 용도고 값을 보내줄 것이 없으니까 redirect를 사용
            return redirect('products:index') # url로 이동시켜줄 뿐(app name:url name) 글작성 후 제출하면 index로 이동
    else: 
        product_form = ProductForm() # post 요청이 아니면(제출 버튼을 안누르면) 빈 폼을 보여줌

    context = {
        "product_form": product_form # 유효하지 않을 때, 사용자의 인풋을 다 받아서, 검증까지 해서 에러메시지를 저장한 product_form(템플릿 내에서 부트스트랩 폼에 사용)
        # post일 때는 post의 product_form이 여기에 해당 되고, 해당 페이지 접속일 (글생성 x)때는 else의 product_form이 들어감
    }

    return render(request, "products/forms.html", context) # 제출에 이슈가 있다면 값을 보내며 다시 폼으로 돌아가기


def detail(request, product_pk): # 요청 받은 것에 product_pk가 포함됨
    product = Product.objects.get(id=product_pk) # id가 요청받은 product_pk가 같은 것을 가져옴

    context = {
        "product":product 
    }

    return render(request, "products/detail.html", context) # 요청 받은 것을 가지고, detail 페이지에 값을 전달


def update(request, product_pk): # url에 product_pk 받아야하므로 요청 받은 것에 product_pk 가포함됨
    product = Product.objects.get(id=product_pk) # id가 요청받은 product_pk가 같은 것을 가져옴

    if request.method == "POST": # 업데이트 제출 버튼 눌렀을 때
        product_form = ProductForm(request.POST, request.FILES, instance=product) # 요청된 포스트와 요청 된 파일, 기존에 모델에 있는 것을 넣어 놓은 것을 요청 된 것으로 바꿈

        if product_form.is_valid(): # 위 폼이 유효하다면
            product_form.save() # 저장

            return redirect("products:detail", product_pk) # 몇번 상품의 디테일 페이지에 보내줄껀지? 
    else:
        product_form = ProductForm(instance=product) # 기존 모델에 저장 되어있는 값을 보여줌

    context = {
        "product_form": product_form # 유효하지 않을 때는 요청 받은 product_form, 제출 안눌렀을 때는 바로위의 폼
    }

    return render(request, "products/forms.html", context) # 유효하지 않을 때나, 제출 안눌렀을 때는 위의 컨텍스트 값을 가져와서 forms.html을 보여줌


def delete(request, product_pk):
    product = Product.objects.get(id=product_pk)
    product.delete()

    return redirect("products:index")


def add_jjim(request, product_pk): # product_pk값을 불러와야 되는 이유는 해당 상품을 장바구니에 넣는 것이니까 
    product = Product.objects.get(id=product_pk) # 특정 상품 가져오고

    if request.user in product.jjim.all(): # 상품에 찜이 되어있는 모든 것 중 요청유저가 있다면
        product.jjim.remove(request.user) # 상품이 요청유저의 찜을 지움
    else: # 누른적이 없는 경우, 
        product.jjim.add(request.user) # 상품이 요청유저에게 찜을 받는다. 
                                     
    return redirect('products:show_jjim', request.user.pk) # detail로 보낼 때는 상품에 대한 pk가 필요하니까 product_pk를 써줌


def show_jjim(request, user_pk):
    jjim = get_user_model().objects.get(id=user_pk)# 특정 유저 데이터를 가지고 오고 
    jjim1 = jjim.jjim_product.all() # 모델.related_name.method()
    # 특정 유저가(user_pk)가 찜한 상품 목록 모두 확인
    context = {
        'jjim': jjim1
    }

    return render(request, 'products/jjim.html', context) # 값을 던져준 html을 보여줌

def delete_jjim(request, product_pk): # 상품에 대한 삭제니까 product_pk기재
    product = Product.objects.get(id=product_pk) 
    product.jjim.remove(request.user) # 상품이 요청유저의 찜을 지움

    return redirect('products:show_jjim', request.user.pk) # 찜리스트 url로 보낼 때는 누구의 찜리스트로 가라는지 필요, show_jjim이라는 url이 user_pk 값을 필요로함, request.user.pk또는 request.user.id 필요
    # redirect 할 때, user_pk가 아닌 request.user.pk를 하는 이유는 호출할때 user_pk호출하지 않고 request, prduct_pk를 호출하기 때문에 request를 붙인 request.user.pk를 사용

def like(request, product_pk):
    product = Product.objects.get(id=product_pk) # 특정 상품 가져오기
    if request.user in product.like_users.all(): # 특정 상품에 좋아요를 한 모든 유저 안에 요청한 유저가 있다면
        # 좋아요 삭제하고
        product.like_users.remove(request.user) # 상품에 요청한 사용자의 좋아요 제거
        is_liked = False
    else: # 요청한 유저가 없다면
        # 좋아요 추가하고 
        product.like_users.add(request.user) # 상품에 요청한 사용의 좋아요 추가
        is_liked = True
    # 상세 페이지로 redirect
    context = {
        'isLiked' : is_liked,
    }
    return JsonResponse(context)


    




    