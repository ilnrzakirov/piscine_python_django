from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(null=False, auto_now_add=True)
    synopsis = models.CharField(null=False, max_length=312)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title


class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title
