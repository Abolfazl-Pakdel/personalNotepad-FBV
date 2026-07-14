from django import forms

from notepad.models import Note


class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    is_pinned = forms.BooleanField(required=False)

    class Meta:
        model = Note
        fields = ['title', 'content', 'is_pinned']