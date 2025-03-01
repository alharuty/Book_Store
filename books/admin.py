from django.contrib import admin
from .models import Book # importamos el modelo Book de models.py

# registrar nuestro modelo Book en el admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('publish_date', 'author')