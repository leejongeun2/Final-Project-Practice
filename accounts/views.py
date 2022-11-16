from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile

# Create your views here.
def signup(request): # 회원가입할 때 프로필을 생성하는 이유는 회원가입 이후 생성 시, 여러번 프로필을 생성할 수 있기 때문에 또 다른 제약을 줘야함(회원가입 시 프로필을 생성하면 딱 한번 만들 수 있기 때문) => 그렇다면 왜? user모델은 장고 내장 된 폼을 받아온 것이기 때문에 프로필 필드가 없음(참조가 필요)
    if request.method == 'POST': # 요청 받아서 제출 누르면
        form = CustomUserCreationForm(request.POST) # 커스텀 폼에 요청 받은 것이 담기고 그것을 폼이란 변수에 저장
        profile_image = Profile() # 프로필 생성
        if form.is_valid(): # 유효하다면 
            user = form.save() # 커스텀 폼에 요청 받은 것을 저장하고 그것을 user에 저장
            profile_image.user = user # 프로필 이미지의 유저가 외래키이기 때문에 user 값이 비어있음, 그것을 생성 된 유저(폼 저장 된 것)으로 지정해줌
            profile_image.save() # 프로필 이미지 저장
            auth_login(request, user) # 로그인함수는 login(request, user) 회원가입과 동시에 로그인됨
            return redirect('products:index') # url로 이동
    else:
        form = CustomUserCreationForm() # post 요청이 아니면(제출 버튼을 안누르면) 빈 폼을 보여줌

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context) # 유효하지 않을 때(post일때), 사용자의 인풋을 다 받아서, 검증까지 해서 에러메시지를 저장한 product_form(템플릿 내에서 부트스트랩 폼에 사용)
    # 해당 페이지 접속일 (글생성 x)때는 else의 product_form이 들어감


def login(request):
    if request.method == 'POST': # 로그인 버튼 누르면
        form = AuthenticationForm(request, data=request.POST) # request를 첫번째 인자로 취함, 유효성 검사를 위해 "data=" 을 통해 판별, 유저가 존재하는지 검증하는 모델폼
        if form.is_valid(): # 유효하면 
            auth_login(request, form.get_user()) # auth_login 함수는 세션에 유저를 기록하는 함수, get_user()는 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환하며, AuthenticationForm의 인스턴스 메서드, 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
            # return redirect(request.GET.get('next') or 'products:index') 
            # http://localhost:8000/accounts/login/?    next = /products/1/update/
            if request.GET.get('next'): # next라면
                return redirect(request.GET.get('next')) # 원래 next url로 가고
            else: # next가 아니라면
                return redirect('products:index') # 정상 로그인이니까 로그인 후 index로 이동을 하기

    else:
        form = AuthenticationForm(request) # 로그인 버튼을 누르지 않으면

    context = {
        'form': form 
    }

    return render(request, 'accounts/login.html', context) # 유효성 검사에 실패하거나, 로그인 페이지 접속만 한 경우, 담긴 값을 가지고 다시 로그인 페이지로 이동


@login_required
def logout(request):
    auth_logout(request) # 요청 유저에 대한 세션 정보를 삭제함, HttpRequest 객체를 인자로 받고 반환 값이 없음
    return redirect('products:index')

@login_required # @안하면 접속이 가능하게 됨, 그러므로 @로 로그인화면이 보여지도록 해야함
def profile(request):
    user_ = get_user_model().objects.get(pk=request.user.pk) # 요청한 유저를 user_로 정의, 해당 함수 인자는 request밖에 없으니까 특정 user를 지칭할때 request.user를 사용(reuqest.user는 get_user_model().objects.get(pk=request.user.pk)와 같음)
    products = user_.product_set.all() # 요청유저가 작성한 모든 상품들 출력하기  
    profile_ = user_.profile_set.all()[0] # 요청유저가 등록한 모든 프로필 출력하기(그 중 제일 먼저 등록한 회원가입 때 것)
    profile_create_form = ProfileForm
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile_)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile_)
    context = {
        "products": products,
        "profile": profile_,
        "profile_update_form":form,
        'profile_create_form':profile_create_form,
    }
    return render(request, 'accounts/profile.html', context) # redirect 사용 시, url의 view가 실행되기 떄문에 render을 써야함(Readme참고)

# def profile_create(request):
#     user_ = get_user_model().objects.get(pk=request.user.pk)
#     profile_form = ProfileForm(request.POST)
#     if profile_form.is_valid():
#         profile = profile_form.save(commit=False)
#         profile.user = user_
#         profile.save()
#     return redirect('accounts:profile')


def profile_update(request):
    user_ = get_user_model().objects.get(pk=request.user.pk) # 요청한 유저 정보 불러오기
    current_user = user_.profile_set.all()[0] # 요청한 유저가 만든 모든 프로필 중 1개를 current_user로 할당(맨 앞것)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=current_user)
    context = {
        "profile_update_form":form,
    }
    return render(request, "accounts/profile_update.html", context)
        




@login_required
def register_seller(request, user_pk): # 몇번 사용자가 true가 될것인지 알아야 하니까 user_pk값을 넣어줌
    user = get_user_model().objects.get(id=user_pk) # id가 요청 받은 user_pk인 것을 가져옴
    user.is_seller = True       # seller = True, customer = False
    user.save()                 

    return redirect('products:index')       