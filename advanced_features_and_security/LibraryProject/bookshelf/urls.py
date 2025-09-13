from django.urls import path
from . import views


urlpatterns = [
    path('books_list/', views.book_list, name = 'book_list'),
    path('book_list/create_book/', views.can_create, name ='create_book'),
    path('book_list/delete_book/', views.can_delete, name = 'delete_book'),
    path('book_list/edit_book/', views.can_edit, name = 'edit_book')
]