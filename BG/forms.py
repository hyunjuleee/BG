from django import forms
from .models import Q, Comment

class ArticleForm(forms.ModelForm):
     
    class Meta():
        model = Q
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment

        exclude = ('article', )