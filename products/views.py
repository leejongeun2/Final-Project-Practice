from django.shortcuts import render


def index(request):
    return render(request, "products/index.html") # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌
    
