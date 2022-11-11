from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = (
            "user",
            "jjim",
            "review",
            "like_users",
        ) # 모델에서 정의했던 것 중에 제외할 필드