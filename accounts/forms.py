from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2',)
    

class ProfileForm(forms.ModelForm): # 사용자로부터 프로필 데이터 입력을 받기 위한 폼 작성
    class Meta:
        model = Profile
        fields = ["image"]
