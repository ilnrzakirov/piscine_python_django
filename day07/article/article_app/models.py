from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64, null=False, verbose_name='Заголовок')
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(null=False, auto_now_add=True, verbose_name='Дата и время создания')
    synopsis = models.CharField(null=False, max_length=312, verbose_name='Краткое описание')
    content = models.TextField(null=False, verbose_name='Контент')

    def __str__(self):
        return self.title


class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title
