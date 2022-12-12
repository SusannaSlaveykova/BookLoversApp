from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from BookLoversApp.accounts.models import AppUser
from BookLoversApp.books.forms import BookCreateForm, BookEditForm
from BookLoversApp.books.models import Book

from django.contrib.auth.decorators import login_required

from BookLoversApp.mixins.OwnerMixins import OwnerRequiredMixin

UserModel = get_user_model()


@login_required(login_url='/accounts/login/')
def add_book(request):
    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('details profile', pk=request.user.pk)
        else:
            return render(request, 'books/book-add-page.html', {'form': form})

    context = {
        'form': form,
    }

    return render(request, 'books/book-add-page.html', context)


class BookDetailsView(views.DetailView):
    model = Book
    template_name = 'books/book-details-page.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['is_owner'] = self.request.user.pk == self.object.user_id

        return context


@login_required(login_url='/accounts/login/')
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if book.user_id is not request.user.id:
        return redirect('no permission')

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)

    context = {
        'form': form,
        'book': book
    }

    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return redirect('details profile', pk=request.user.pk)
    else:
        return render(request, 'books/book-edit-page.html', context)


def added_books_by_user(request, user_pk):
    creator_of_post = AppUser.objects.get(pk=user_pk)
    all_books = Book.objects.all()
    books_added_by_user = all_books.filter(user_id=creator_of_post.id)

    context = {
        'books_added_by_user': books_added_by_user,
        'user': creator_of_post,

    }

    return render(request, 'books/book_list_by_user.html', context)


class BookDeleteView(OwnerRequiredMixin, views.DeleteView):
    context_object_name = 'book'
    model = Book
    template_name = 'books/book-delete-page.html'
    fields = ()
    success_url = reverse_lazy('show index')
