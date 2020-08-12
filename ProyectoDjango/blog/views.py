from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article

# Create your views here.
def list(request):
    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': articles
    })

def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category,id=category_id)

    return render(request, 'categories/category.html', {
        'title': 'Categorias',
        'category': category
    })
