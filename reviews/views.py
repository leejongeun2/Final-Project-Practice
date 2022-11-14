from django.shortcuts import render, redirect
from products.models import Product
from .forms import ReviewForm
from .models import Review
# Create your views here.

def index(request, product_pk):
    product = Product.objects.get(id=product_pk) # 특정상품 가져오고
    reviews = product.review.all() # 정참조이며, 특정 상품에 쓰인 리뷰 모두 확인
    form = ReviewForm(instance=product) # 특정 상품 모델 정보(리뷰도 포함)를 리뷰 폼에 넣어줌

    context = {
        'reviews': reviews,
        'product_pk': product_pk,
        'form' : form,
    }
    
    return render(request, 'reviews/index.html', context)


def create(request, product_pk): # url에 product_pk가 있어서 넣어줘야함
    product = Product.objects.get(id=product_pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES) # 사용자가 요청한 post와 이미지를 불러옴

        if form.is_valid(): # post 이고 유효하면
            review = form.save(commit=False) # 저장을 잠깐 멈추고
            review.user = request.user # 리뷰 작성자를 요청한 사람으로 정의 => 리뷰 user_id에 저장되어야 할 작성자 정보가 누락되었기 때문
           
            if request.user not in product.review.all(): # 정참조, 상품에 쓰인 전체 리뷰 중 요청자가 포함되어있지 않다면
                 review.save() # 리뷰 저장
                 product.review.add(review) # 특정 상품의 리뷰를 작성한다. 
            # else:
                # 실패 alert 가 뜨게 만들어야함.

            return redirect('reviews:index', product_pk)

    else: # 작성 제출 버튼 누르지 않으면
        form = ReviewForm() # 빈 폼을 보여줌

    context = {
        'form': form # post일 때는 post의 form이 여기에 해당 되고, 해당 페이지 접속일 (글생성 x)때는 else의 form이 들어감
    }

    return render(request, 'reviews/forms.html', context)