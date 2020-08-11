from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:param_slug>', views.page, name='page')
]

