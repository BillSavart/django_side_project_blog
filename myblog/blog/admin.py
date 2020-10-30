from django.contrib import admin
from .models import Author, Article, Reply

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Reply)