from django import forms

from BookLoversApp.common.models import Comment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Your comment here:'}),

        }
        labels = {
            'comment': "Comment",

        }


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Your comment here:'}),

        }
        labels = {
            'comment': "Comment",

        }
