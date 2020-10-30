from django.shortcuts import render
from .models import Author, Article, Reply
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView

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
    paginate_by = 4

class ArticleContextView(generic.DetailView):
    """Generic class-based detail view for an article."""
    model = Article

"""
class ReplyCreate(LoginRequiredMixin, CreateView):
    """Form for adding a reply. Requires login."""
    model = Reply
    fields = ['context',]

    def get_context_data(self, **kwargs):
        """Add associated blog to form template so can display its title in HTML"""
        # Call the base implementation first to get a context
        context = super(ReplyCreate, self).get_context_data(**kwargs)

        # Get the blog from id and add it to the context
        context['article'] = get_object_or_404(Article, pk = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        """Add author and associated blog to form data before setting it as valid (so it is saved to model)"""
        # Add logged-in user as author of reply
        form.instance.author = self.request.user

        # Associate reply with blog based on passed id
        form.instance.article = get_object_or_404(Article, pk = self.kwargs['pk'])

        # Call super-class form validation behaviour
        return super(ReplyCreate, self).form_valid(form)

    def get_success_url(self):
        """After posting reply return to associated blog."""
        return reverse('article-context', kwargs={'pk': self.kwargs['pk'],})
"""
