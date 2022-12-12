from django.contrib.auth.decorators import login_required
from django.urls import path

from BookLoversApp.accounts.views import SignUpView, SignInView, SignOutView, UserDetailsView,\
    UserDeleteView, no_permission, UserEditView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserDetailsView.as_view(), name='details profile'),
    path('profile/<int:pk>/edit/', login_required(UserEditView.as_view()), name='edit profile'),
    path('profile/<int:pk>/delete/', UserDeleteView.as_view(), name='delete profile'),
    path('no_permission', no_permission, name='no permission')
)
