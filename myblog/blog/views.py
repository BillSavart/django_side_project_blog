from django.shortcuts import render
from .models import User, Article
from django.views import generic

# Create your views here.
def index(request):
    """View function for the home page"""
    num_article = Article.objects.all().count()
    num_user = User.objects.all().count()

    return render(
        request,
        'index.html',
        context = {
            'num_article': num_article,
            'num_user': num_user,
        }
    )

class ArticleView(generic.ListView):
    """Generic class-based view for a list of articles"""
    model = Article
    paginate_by = 5

class ArticleContextView(generic.DetailView):
    """Generic class-based detail view for an article."""
    model = Article