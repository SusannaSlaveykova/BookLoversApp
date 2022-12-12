from django.contrib.auth.decorators import login_required
from django.urls import path

from BookLoversApp.accounts.views import no_permission
from BookLoversApp.beloved_characters.views import add_beloved_character, edit_beloved_character,\
    current_user_beloved_characters, current_book_beloved_characters, DeleteBelovedCharacterView

urlpatterns =(
    path('add/<int:book_pk>', add_beloved_character, name='add beloved character'),
    # path('details/<int:pk>', details_of_beloved_character, name='details of beloved character'),
    path('edit/<int:char_pk>', edit_beloved_character, name='edit beloved character'),
    path('delete/<int:pk>', login_required(DeleteBelovedCharacterView.as_view()), name='delete beloved character'),
    path('beloved_characters_by_user/<int:user_pk>', current_user_beloved_characters, name='beloved characters list by user'),
    path('beloved_users_by_book/<int:book_pk>', current_book_beloved_characters, name='beloved characters list by book'),

)
