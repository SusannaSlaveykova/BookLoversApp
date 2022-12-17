from django import forms
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, PasswordInput
from django.shortcuts import render

from BookLoversApp.books.models import Book

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password:'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repeat password:'}))

    class Meta:
        model = UserModel
        fields = ("username", 'email', 'password1', 'age', 'gender',)
        field_classes = {"username": auth_forms.UsernameField}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username:'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email:'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age:'})
        }


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username:'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password:'}))


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'profile_picture', 'age', 'gender', )
        field_classes = {"username": auth_forms.UsernameField}
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name:'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name:'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email:'}),
            'age': forms.TextInput(attrs={'placeholder': 'Your age:'}),
        }

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'age': 'Age'
        }


class UserDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['books'] = Book.objects.all()
        return context
