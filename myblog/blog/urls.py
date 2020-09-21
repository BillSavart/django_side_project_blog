from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>', views.ArticleContextView.as_view(), name='article-context'),
]