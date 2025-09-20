from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=230)
    author = models.CharField(max_length=150)

    def __str__(self):
        return f"title: {self.title} \n author: {self.author}"