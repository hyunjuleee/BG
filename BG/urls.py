from django.urls import path
from . import views

app_name = 'BG'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_id>/commrnts/create/', views.comment_create, name='comment_create')
]