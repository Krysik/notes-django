from django import forms
from .models import Note


class AddNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddNoteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Tytuł'
        self.fields['content'].label = 'Treść'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Note
        fields = ('title', 'content')