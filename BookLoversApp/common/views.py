from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from BookLoversApp.books.models import Book
from BookLoversApp.common.forms import CommentCreateForm, CommentEditForm
from BookLoversApp.common.models import Comment
from BookLoversApp.mixins.OwnerMixins import OwnerRequiredMixin

UserModel = get_user_model()


def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'common/home-page.html', context)


@login_required(login_url='/accounts/login/')
def add_comment(request, book_pk):
    to_book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        form = CommentCreateForm()
    else:
        form = CommentCreateForm(request.POST)
    context = {
        'form': form,
        'to_book': to_book,
    }
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.book = to_book
        comment.save()

        return redirect('details profile', pk=request.user.pk)

    else:
        return render(request, 'common/comments-add-page.html', context)


def comments_by_user(request, user_pk):
    user = UserModel.objects.get(pk=user_pk)
    comments = user.comment_set.all().order_by('date_and_time_of_publication')
    context = {
        'user': user,
        'comments': comments,

    }

    return render(request, 'common/comment_list_by_user.html', context)


def comments_by_book(request, book_pk):
    book = Book.objects.get(pk=book_pk)

    comments = book.comment_set.all().order_by('comment')
    context = {
        'book': book,
        'comments': comments,

    }
    return render(request, 'common/comment-list.html', context)


@login_required(login_url='/accounts/login/')
def edit_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if comment.user_id is not request.user.id:
        return redirect('no permission')

    if request.method == 'GET':
        form = CommentEditForm(instance=comment)
    else:
        form = CommentEditForm(request.POST, instance=comment)
    context = {
        'form': form,
        'comment': comment,
    }
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
        return redirect('details profile', pk=request.user.pk)
    else:
        return render(request, 'common/comment-edit-page.html', context)


class CommentDeleteView(OwnerRequiredMixin, views.DeleteView):
    context_object_name = 'comment'
    model = Comment
    template_name = 'common/comment-delete-page.html'
    fields = ()
    success_url = reverse_lazy('show index')
