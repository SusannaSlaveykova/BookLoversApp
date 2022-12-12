from django.contrib.auth.decorators import login_required
from django.urls import path

from BookLoversApp.quotes.views import add_quote, edit_quote, current_book_quotes, \
    current_user_quotes, DeleteQuoteView

urlpatterns =(
    path('add_to_book/<int:book_pk>/', add_quote, name='add quote'),
    path('quotes_list_by_user/<int:user_pk>', current_user_quotes, name='quotes list by user'),
    path('quotes_list_by_book/<int:book_pk>', current_book_quotes, name='quotes list'),

    path('edit_quote/<int:quote_pk>', edit_quote, name='edit quote'),
    path('delete_quote/<int:pk>', login_required(DeleteQuoteView.as_view()), name='delete quote'),
)
