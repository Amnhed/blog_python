from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def list(request):
    articles = Article.objects.all()

    #Paginar los articulos cada dos
    paginator = Paginator(articles, 2)

    # Recoger numero de paginay enviar para obtener los articulos paginados por cada pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': page_articles
    })

@login_required(login_url="login")
def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category,id=category_id)
    articles = Article.objects.filter(categories=category)

    return render(request, 'categories/category.html', {
        'title': 'Categorias',
        'category': category,
        #'articles':articles
    })

@login_required(login_url="login")    
def article(request, article_id):

    article = get_object_or_404(Article,id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article
    })


