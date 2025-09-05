from django.contrib import admin

# Register your models here.
from .models import Book

class bookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
    

admin.site.register(Book, bookAdmin)