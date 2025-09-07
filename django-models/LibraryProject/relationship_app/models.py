from django.db import models

# Create your models here.
from django.contrib.auth.models import User

######################################################################################

#####################################################################################




class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_name')

    def __str__(self):
        return f"title: {self.title} author: {self.author.name}" 

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='genre')

    def __str__(self):
        return f"lib_name: {self.name} books: {self.books})"

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.library}"

############################################################################    
#Testing this out 
class UserProfile(models.Model):
    ROLE_CHOICES = (("Admin","Admin"),
                    ("Librarian", "Librarian"),
                    ("Member", "Member"),
                    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_task")
    assignees = models.ManyToManyField(User, related_name="assigned_tasks")

    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [("can_assign_task", "Can_assign_to_other_users")]
    
##########################################################################

###########################################################################
#Trying chat code for Task 2


############################################################################