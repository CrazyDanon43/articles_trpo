from django.shortcuts import render, get_object_or_404, redirect
from .models import Article


def article_list(request):
    """Отображение списка всех статей"""
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_create(request):
    """Создание новой статьи"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            article = Article.objects.create(title=title, content=content)
            return redirect('article_list')

    return render(request, 'articles/article_form.html', {'action': 'create'})


def article_edit(request, id):
    """Редактирование существующей статьи"""
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_list')

    return render(request, 'articles/article_form.html', {'article': article, 'action': 'edit'})