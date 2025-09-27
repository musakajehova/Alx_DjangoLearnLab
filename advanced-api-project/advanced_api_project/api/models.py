from django.db import models

# Create your models here.

class Author(models.Model):
    """This model is the Author model"""
    author = models.CharField(max_length=150)

    def __str__(self):
        return f"Author: {self.author}"

class Book(models.Model):
    """This is a Book model, the author field is a foreign key from the author model"""
    title = models.CharField(max_length=250)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title} /n Publication Year: {self.publication_year} /n Author: {self.author}"
