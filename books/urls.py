from django.contrib import admin # importamos admin
from django.urls import path # importamos path
from .views import getAllBooks, createBook, updateBook, book_details # importamos las funciones que hemos creado en views.py

urlpatterns = [
    path('', getAllBooks, name='books'),
    path('createbook/', createBook, name='createbook'),
    path('updatebook/<int:id>', updateBook, name='updatebook'),
    path('book_details/<int:id>', book_details, name='book_details'),
]
