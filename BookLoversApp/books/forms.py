from django import forms

from BookLoversApp.books.models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pages', 'year_of_first_publication', 'cover_photo', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title:'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author:'}),
            'pages': forms.TextInput(attrs={'placeholder': 'Pages:'}),
            'year_of_first_publication': forms.NumberInput(attrs={'placeholder': 'Year of first publication:'}),
            'cover_photo': forms.URLInput(attrs={'placeholder': 'URL to picture:'}),
            'description': forms.Textarea(attrs={'placeholder': 'Book description:'}),

        }
        labels = {
            'title': "Title",
            'author': 'Author',
            'pages': 'Pages',
            'year_of_first_publication': 'Year:',
            'cover_photo': 'URL to picture',
            'description': 'Book description'

        }


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pages', 'year_of_first_publication', 'cover_photo', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title:'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author:'}),
            'pages': forms.TextInput(attrs={'placeholder': 'Pages:'}),
            'year_of_first_publication': forms.TextInput(attrs={'placeholder': 'Year of first publication:'}),
            'cover_photo': forms.TextInput(attrs={'placeholder': 'URL to picture:'}),
            'description': forms.Textarea(attrs={'placeholder': 'Book description:'}),

        }
        labels = {
            'title': "Title",
            'author': 'Author',
            'pages': 'Pages',
            'year_of_first_publication': 'Year:',
            'cover_photo': 'URL to picture',
            'description': 'Description'

        }

