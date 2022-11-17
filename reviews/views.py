from django.shortcuts import render, redirect
from products.models import Product
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request, product_pk):
    product = Product.objects.get(id=product_pk) # 특정상품 가져오고
    reviews = product.review.all() # 정참조이며, 특정 상품에 쓰인 리뷰 모두 확인
    # form = ReviewForm(instance=product) # 리뷰 폼을 인덱스에서 사용할 때 쓰는 것, 인스턴스에 product를 넣은 경우, 리뷰 폼과 상품 폼에서 겹치는 content가 들어가져있는 것으로 보여짐

    context = {
        'reviews': reviews,
        'product': product,
        # 'form' : form,
    }
    
    return render(request, 'reviews/index.html', context)


def create(request, product_pk): # url에 product_pk가 있어서 넣어줘야함
    product = Product.objects.get(id=product_pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES) # 사용자가 요청한 post와 이미지를 불러옴

        if form.is_valid(): # post 이고 유효하면
            review = form.save(commit=False) # 저장을 잠깐 멈추고
            review.user = request.user # 리뷰 작성자를 요청한 사람으로 정의 => 리뷰 user_id에 저장되어야 할 작성자 정보가 누락되었기 때문
            review.save() # 리뷰 저장
            product.review.add(review) # 특정 상품의 리뷰를 작성한다. 

            return redirect('reviews:index', product_pk)

    else: # 작성 제출 버튼 누르지 않으면
        form = ReviewForm() # 빈 폼을 보여줌

    context = {
        'form': form # post일 때는 post의 form이 여기에 해당 되고, 해당 페이지 접속일 (글생성 x)때는 else의 form이 들어감
    }

    return render(request, 'reviews/forms.html', context)

def update(request, review_pk): # url에 있는 review_pk를 인자로 가져옴
    review = Review.objects.get(id=review_pk) # id가 가져온 review_pk에 해당 하는 것을 review로 할당
    product_pk = review.review_product.get().id


    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)

        if form.is_valid():
            review = form.save(commit=False) # save잠깐 멈추고
            review.user = request.user # 요청자가 리뷰 유저라고 지정해줌
            review.save()
           

            return redirect('reviews:index', product_pk) # 역참조, 특정리뷰가 작성 된 상품 id를 가져온다.== product_pk

    else:
        form = ReviewForm(instance=review) # 수정 제출 버튼 안눌렀다면 기존 작성되어 모델에 저장 된 리뷰가 보여짐

    context = {
        'form': form # 1.유효하지 않을떄, 2.수정버튼 안눌렀을 때
    }

    return render(request, 'reviews/forms.html', context) 


def delete(request, review_pk):
    review = Review.objects.get(id=review_pk)
    product_pk = review.review_product.get().id
    review.delete()

    return redirect('reviews:index', product_pk)

            
