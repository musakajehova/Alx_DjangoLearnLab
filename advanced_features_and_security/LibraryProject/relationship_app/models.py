from django.db import models

# Create your models here.
#rom django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

######################################################################################
from django.contrib.auth.models import BaseUserManager ,AbstractUser
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
    
    class Meta:
        permissions = [("can_add_book", "can_add_book"),
                       ("can_change_book", "can_change_book"),
                       ("can_delete_book", "can_delete_book"),

        ]

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

############################################################################################################
    #Creating an Abstract User

class MyUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField()

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            #profile_photo=profile_photo
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, date_of_birth, password=None):

        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            #profile_photo=profile_photo
        )
        user.is_admin = True
        user.save(using=self._db)
        return user