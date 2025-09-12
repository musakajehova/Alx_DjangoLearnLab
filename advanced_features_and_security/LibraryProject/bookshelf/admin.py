from django.contrib import admin

# Register your models here.
from .models import Book, MyUser

################################################################################
from django.contrib.auth.admin import UserAdmin
###############################################################################

class bookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
    

admin.site.register(Book, bookAdmin)

admin.site.register(MyUser, UserAdmin)