from django import forms

from BookLoversApp.beloved_characters.models import BelovedCharacter


class FavCharCreateForm(forms.ModelForm):
    class Meta:
        model = BelovedCharacter
        fields = ('name', 'reason_to_like', 'favourite_story',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name:'}),
            'reason_to_like': forms.TextInput(attrs={'placeholder': 'Reason to like:'}),
            'favourite_story': forms.Textarea(attrs={'placeholder': 'Favourite story:'}),

        }
        labels = {
            'name': "Name",
            'reason_to_like': "Reason to like",
            'favourite_story': 'Favourite story',

        }


class FavCharEditForm(forms.ModelForm):
    class Meta:
        model = BelovedCharacter
        fields = ('name', 'reason_to_like', 'favourite_story',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name:'}),
            'reason_to_like': forms.TextInput(attrs={'placeholder': 'Reason to like:'}),
            'favourite_story': forms.Textarea(attrs={'placeholder': 'Favourite story:'}),

        }
        labels = {
            'name': "Name",
            'reason_to_like': "Reason to like",
            'favourite_story': 'Favourite story',

        }
