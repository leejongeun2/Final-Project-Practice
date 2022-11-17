from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    star_list = [
        ('-', '-'),
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), 
    ]
    star = forms.ChoiceField(choices=star_list, 
            widget=forms.Select(
            attrs={
                'placeholder': 'Enter the star',
                'style': 'background-color: black; color: white; border-color: #FA6EE3;',
                }
            ),
        )
    
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
    
    class Meta:
        model = Review
        
        exclude = (
            'user',
        )