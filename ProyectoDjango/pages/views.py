from django.shortcuts import render
from .models import Page

# Create your views here.
def page(request,param_slug):
    #obtengo el slug de urls.py slug_bd =slug_parametro url
    page = Page.objects.get(slug=param_slug)

    return render(request, "pages/page.html",{
        "page": page
    })