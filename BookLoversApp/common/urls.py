from django.contrib.auth.decorators import login_required
from django.urls import path

from BookLoversApp.common.views import index, add_comment, comments_by_user, comments_by_book, edit_comment, \
    CommentDeleteView

urlpatterns =(
    path('', index, name='show index'),
    path('add_to_book/<int:book_pk>/', add_comment, name='add comment'),
    path('comments_list_by_user/<int:user_pk>', comments_by_user, name='comment list by user'),
    path('comments_by_book/<int:book_pk>', comments_by_book, name='comment list by book'),

    path('edit_comment/<int:comment_pk>', edit_comment, name='edit comment'),
    path('delete_comment/<int:pk>', login_required(CommentDeleteView.as_view()), name='delete comment'),

)