from django import forms
from .models import Q, Comment, Q_Comment

class ArticleForm(forms.ModelForm):
    class Meta():
        model = Q
        fields = '__all__'
        widgets = {
            '제목': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            '보기A': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            '보기B': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Q_Comment

        exclude = ('Q_article', )
        widgets = {
            '답변': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),

            '내용': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'cols': 50,
                }
            ),
        }

        