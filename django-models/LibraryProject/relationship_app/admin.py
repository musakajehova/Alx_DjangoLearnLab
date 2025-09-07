from django.contrib import admin

# Register your models here.
from .models import Author, Book, Library, Librarian

"""class bookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
""" 

admin.site.register(Author) 
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)