from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    """A model to define a user of the blog"""
    name = models.CharField(max_length=20, help_text='Register your username(Less than 20 letters)')
    register_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        """String for representing the model object"""
        return self.name


class Article(models.Model):
    """A model to define a article written by a user"""
    title = models.CharField(max_length=50, help_text='Title of the article up to 50 letters')
    context = models.TextField(help_text='Enter your context here')
    points = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular article context."""
        return reverse('article-context', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

"""
class Reply(models.Model):
    """A model to define a reply of an article"""
    author = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reply')
    #upload_time = models.DateTimeField(auto_now_add=True)
    context = models.TextField(max_length=1000)

    def __str__(self):
        """String for representing the Model object."""
        return self.context

"""
