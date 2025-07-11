from django import forms

from events.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'description']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
