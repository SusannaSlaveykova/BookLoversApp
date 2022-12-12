from django import forms

from BookLoversApp.quotes.models import Quote


class QuoteCreateForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('quote_text',)
        widgets = {
            'quote_text': forms.Textarea(attrs={'placeholder': 'Type your favourite quote here:'})
        }
        labels = {
            'quote_text': "Quote",

        }


class QuoteEditForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('quote_text',)
        widgets = {
            'quote_text': forms.Textarea(attrs={'placeholder': 'Type your favourite quote here:'})
        }
        labels = {
            'quote_text': "Quote",

        }
