from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from BookLoversApp.books.models import Book
from BookLoversApp.mixins.OwnerMixins import OwnerRequiredMixin
from BookLoversApp.quotes.forms import QuoteCreateForm, QuoteEditForm
from BookLoversApp.quotes.models import Quote
from django.views import generic as views

UserModel = get_user_model()


@login_required(login_url='/accounts/login/')
def add_quote(request, book_pk):
    try:
        to_book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExist as ex:
        return render(request, 'Errors.html')
    if request.method == 'GET':
        form = QuoteCreateForm()
    else:
        form = QuoteCreateForm(request.POST)
        quote = form.save(commit=False)
        quote.user = request.user
        quote.book = to_book
        quote.save()

        return redirect('details profile', pk=request.user.pk)

    context = {
        'form': form,
        'to_book': to_book,
    }

    return render(request, 'quotes/quotes-add-page.html', context)


@login_required(login_url='/accounts/login/')
def edit_quote(request, quote_pk):
    try:
        quote = Quote.objects.get(pk=quote_pk)
    except Quote.DoesNotExist as ex:
        return render(request, 'Errors.html')

    if quote.user_id is not request.user.id:
        return redirect('no permission')

    if request.method == 'GET':
        form = QuoteEditForm(instance=quote)
    else:
        form = QuoteEditForm(request.POST, instance=quote)
    context = {
        'form': form,
        'quote': quote,
    }
    if form.is_valid():
        quote = form.save(commit=False)
        quote.user = request.user
        try:
            quote.save()
            return redirect('details profile', pk=request.user.pk)
        except Exception as ex:
            return HttpResponse('error 400')



    else:

        return render(request, 'quotes/quotes-edit-page.html', context)


class DeleteQuoteView(OwnerRequiredMixin, views.DeleteView):
    context_object_name = 'quote'
    model = Quote
    template_name = 'quotes/quotes-delete-page.html'
    fields = ()
    success_url = reverse_lazy('show index')


def current_book_quotes(request, book_pk):
    try:
        book = Book.objects.get(pk=book_pk)

        quotes = book.quote_set.all().order_by('date_and_time_of_publication')
        context = {
            'book': book,
            'quotes': quotes,

        }
        return render(request, 'quotes/quotes-list.html', context)
    except Book.DoesNotExist as ex:
        return render(request, 'Errors.html')


def current_user_quotes(request, user_pk):
    try:
        user = UserModel.objects.get(pk=user_pk)
        quotes = user.quote_set.all().order_by('date_and_time_of_publication')
        context = {
            'user': user,
            'quotes': quotes,
            'is_owner': user_pk == request.user.pk

        }
    except UserModel.DoesNotExist as ex:
        return render(request, 'Errors.html')

    return render(request, 'quotes/quotes_list_by_user.html', context)
