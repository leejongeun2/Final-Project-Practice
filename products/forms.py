from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    content = forms.CharField(
            widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the content',
                'style': 'background-color: black; color: white; border-color: #FA6EE3;',
                'rows': 7,
                'cols': 50,
                }
            ),
        )
    name = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the name',
                'style': 'background-color: black; color: white; border-color: #FA6EE3;',
                }
            ),
        )
    price = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the price',
                'style': 'background-color: black; color: white; border-color: #FA6EE3;',
                }
            ),
        )
    # image = forms.ImageField(
    #         widget=forms.ImageField(
    #         attrs={
    #             'placeholder': 'Enter the image',
    #             'style': 'background-color: black;',
    #             }
    #         ),
    #     )
    class Meta:
        model = Product
        exclude = (
            "user",
            "jjim",
            "review",
            "like_users",
        ) # 모델에서 정의했던 것 중에 제외할 필드