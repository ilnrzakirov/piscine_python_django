from django.contrib.auth.models import User
from django.db import models

class UpVoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class DownVoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Tip(models.Model):
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    upVoice = models.ManyToManyField(UpVoice)
    downVoice = models.ManyToManyField(DownVoice)

