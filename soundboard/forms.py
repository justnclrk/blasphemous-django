from django import forms
from .models import Sound


class SoundCreationForm(forms.ModelForm):
    class Meta:
        model = Sound
        fields = ['location', 'mood']
