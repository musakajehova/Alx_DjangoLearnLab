from django.db import models
from django.conf import settings 
# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.title} by {self.author} "

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Comment by {self.author} on {self.post.id}"