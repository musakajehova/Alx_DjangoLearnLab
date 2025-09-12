from django.contrib import admin

# Register your models here.
from .models import Author, Book, Library, Librarian, UserProfile, Task, MyUser
from django.contrib.auth.admin import UserAdmin

"""class bookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
""" 

admin.site.register(Author) 
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(MyUser, UserAdmin)

