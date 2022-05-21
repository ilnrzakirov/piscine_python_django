from django.contrib.auth.models import User
from django.db import models


class Tip(models.Model):
    content = models.CharField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
