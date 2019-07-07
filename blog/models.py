from django.db import models

# Create your models here.
from django.urls import reverse

from blog_auth.models import MyUser


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='media', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
