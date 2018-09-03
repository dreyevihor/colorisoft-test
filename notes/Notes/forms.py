from django.forms import ModelForm
from Notes.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text']