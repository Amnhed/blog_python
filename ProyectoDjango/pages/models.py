from django.db import models 
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    title = models.CharField(unique=True, max_length=50, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name="Url amigable")
    order = models.IntegerField(default=0, verbose_name="Orden")
    visible = models.BooleanField(verbose_name="Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Pagina"
        verbose_name = "Páginas"
    
    def __str__(self):
        return self.title
