from distutils.command.upload import upload

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail',args=[str(self.id)])   
class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        null = True,
        related_name='comments',
        on_delete=models.CASCADE
    )
    comment = models.CharField(max_length=400, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null = True
    )
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')
             
