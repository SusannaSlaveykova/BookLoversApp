from django.contrib.auth.decorators import login_required
from django.urls import path

from BookLoversApp.books.views import edit_book, BookDetailsView, add_book, BookDeleteView, added_books_by_user

urlpatterns =(
    path('add/', add_book, name='add book'),
    path('details/<int:pk>', BookDetailsView.as_view(), name='details book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('delete/<int:pk>', login_required(BookDeleteView.as_view()), name='delete book'),
    path('added_books_by_user/<int:user_pk>', added_books_by_user, name='added books by user'),

)