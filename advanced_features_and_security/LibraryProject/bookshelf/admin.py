from django.contrib import admin

# Register your models here.
from .models import Book, CustomUser

################################################################################
#from django.contrib.auth.admin import CustomUserAdmin
###############################################################################

class bookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')


class MyUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('email', 'date_of_birth', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'date_of_birth')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )
    

admin.site.register(Book, bookAdmin)

admin.site.register(CustomUser, CustomUserAdmin)