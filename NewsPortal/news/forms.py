from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    header = forms.CharField(max_length=64)
    text = forms.CharField(min_length=30)
    
    class Meta:
        model = Post
        fields = [
            'author',
            'category_type',
            'header',
            'categories',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        header = cleaned_data.get('header')

        if header == text:
            raise ValidationError(
                'The text should not be identical to the header'
            )

        return cleaned_data
