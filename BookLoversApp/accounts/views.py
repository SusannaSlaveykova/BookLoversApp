
from django.contrib.auth import views as auth_view, get_user_model, login

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from BookLoversApp.accounts.forms import SignUpForm, SignInForm, UserEditForm
from BookLoversApp.beloved_characters.models import BelovedCharacter
from BookLoversApp.books.models import Book
from BookLoversApp.common.models import Comment
from BookLoversApp.mixins.OwnerMixins import OwnerRequiredMixin, UserRequiredMixin
from BookLoversApp.quotes.models import Quote

UserModel = get_user_model()


class SignUpView(views.CreateView):
    model = UserModel
    form_class = SignUpForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('show index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_view.LoginView):
    model = UserModel
    form_class = SignInForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('show index')


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('show index')


class UserDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['books'] = Book.objects.filter(user_id=self.object)
        context['quotes'] = Quote.objects.filter(user_id=self.object)
        context['beloved_character_list'] = BelovedCharacter.objects.filter(user_id=self.object)
        context['comments'] = Comment.objects.filter(user_id=self.object)
        return context


class UserEditView(UserRequiredMixin, views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.object.pk})


class UserDeleteView(UserRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('show index')


def no_permission(request):
    return render(request, 'accounts/No-Permission.html')
