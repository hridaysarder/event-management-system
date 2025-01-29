from django import forms
from events.models import Event, Participant, Category

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category', 'participants']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']