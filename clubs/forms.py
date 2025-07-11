from django import forms

from events.models import Event


class ClubBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('club', 'creator',)

