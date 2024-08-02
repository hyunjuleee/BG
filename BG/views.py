from django.shortcuts import render, redirect
from .models import Q, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Q.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    articles = Q.objects.get(id=id)
    form = CommentForm()

    comments = Comment.objects.filter(article_id=id)

    context = {
        'article': articles,
        'form': form,
        'comments': comments,
    }

    return render(request, 'detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    
    return render(request, 'form.html', context)