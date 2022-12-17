from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from BookLoversApp.beloved_characters.forms import FavCharCreateForm, FavCharEditForm
from BookLoversApp.beloved_characters.models import BelovedCharacter
from BookLoversApp.books.models import Book
from BookLoversApp.mixins.OwnerMixins import OwnerRequiredMixin

UserModel = get_user_model()


@login_required(login_url='/accounts/login/')
def add_beloved_character(request, book_pk):
    try:
        to_book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExist as ex:
        return render(request, 'Errors.html')

    if request.method == 'GET':
        form = FavCharCreateForm()
    else:
        form = FavCharCreateForm(request.POST)

    context = {
        'form': form,
        'book': to_book
    }

    if form.is_valid():
        favourite_character = form.save(commit=False)
        favourite_character.user = request.user
        favourite_character.book = to_book
        favourite_character.save()
        return redirect('details profile', pk=request.user.pk)
    else:
        return render(request, 'beloved_characters/beloved-characters-add-page.html', context)


# def details_of_beloved_character(request, pk):
#     return render(request, 'beloved_characters/beloved-character-details-page.html')


@login_required(login_url='/accounts/login/')
def edit_beloved_character(request, char_pk):
    try:
        beloved_character = BelovedCharacter.objects.get(pk=char_pk)
        creator_of_book_id = beloved_character.user_id
    except BelovedCharacter.DoesNotExist as ex:
        return render(request, 'Errors.html')

    if not request.user.id == creator_of_book_id:
        return redirect('no permission')
    beloved_character = BelovedCharacter.objects.get(pk=char_pk)
    if request.method == 'GET':
        form = FavCharEditForm(instance=beloved_character)
    else:
        form = FavCharEditForm(request.POST, instance=beloved_character)

    context = {
        'form': form,
        'beloved_character': beloved_character,
    }
    if form.is_valid():

        beloved_character = form.save(commit=False)
        beloved_character.user = request.user
        beloved_character.save()
        return redirect('details profile', pk=request.user.pk)
    return render(request, 'beloved_characters/beloved-characters-edit-page.html', context)


def current_user_beloved_characters(request, user_pk):
    try:
        user = UserModel.objects.get(pk=user_pk)
        beloved_characters = user.belovedcharacter_set.all().order_by('name')
        context = {
            'user': user,
            'beloved_characters': beloved_characters,
        }
    except UserModel.DoesNotExist as ex:
        return render(request, 'Errors.html')

    return render(request, 'beloved_characters/beloved_character_list_by_user.html', context)


def current_book_beloved_characters(request, book_pk):
    try:

        book = Book.objects.get(pk=book_pk)
        beloved_characters = book.belovedcharacter_set.all().order_by('name')
        context = {
            'book': book,
            'beloved_characters': beloved_characters
        }
    except Book.DoesNotExist as ex:
        return render(request, 'Errors.html')
    return render(request, 'beloved_characters/beloved_character_list_by_book.html', context)


class DeleteBelovedCharacterView(OwnerRequiredMixin, views.DeleteView):
    context_object_name = 'beloved_character'
    model = BelovedCharacter
    template_name = 'beloved_characters/beloved-characters-delete-page.html'
    fields = ()

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.request.user.pk})
