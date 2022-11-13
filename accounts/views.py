from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST': # 요청 받아서 제출 누르면
        form = CustomUserCreationForm(request.POST) # 커스텀 폼에 요청 받은 것이 담기고 그것을 폼이란 변수에 저장
        if form.is_valid(): # 유효하다면 
            form.save() # 저장하고 
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
            auth_login(request, form.get_user()) # auth_login 함수는 세션에 유저를 기록하는 함수, AuthenticationForm의 인스턴스 메서드, 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
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
     return render(request, 'accounts/profile.html') # redirect 사용 시, url의 view가 실행되기 떄문에 render을 써야함(Readme참고)

@login_required
def register_seller(request, user_pk): # 몇번 사용자가 true가 될것인지 알아야 하니까 user_pk값을 넣어줌
    user = get_user_model().objects.get(id=user_pk) # id가 요청 받은 user_pk인 것을 가져옴
    user.is_seller = True       # seller = True, customer = False
    user.save()                 

    return redirect('products:index')       