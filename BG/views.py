from django.shortcuts import render, redirect
from .models import Q, Comment, Q_Comment
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

    comments = Q_Comment.objects.filter(Q_article_id=id)

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
            return redirect('BG:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    
    return render(request, 'form.html', context)

def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.Q_article_id = article_id
            comment.save()

            return redirect('BG:detail', id=article_id)

    else:
        return redirect('BG:index')