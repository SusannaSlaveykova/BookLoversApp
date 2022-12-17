from django.contrib import admin

from BookLoversApp.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pages', 'year_of_first_publication', 'cover_photo']
    ordering = ['title']
    list_filter = ['title', 'author']
    search_fields = ['title']