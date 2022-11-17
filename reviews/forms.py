from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    star = forms.CharField(
            widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the star',
                'style': 'background-color: black; color: white; border-color: #FA6EE3;',
                }
            ),
        )
    class Meta:
        model = Review
        
        exclude = (
            'user',
        )