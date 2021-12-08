from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    message = forms.CharField(label='', min_length=40, max_length=2800,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'maxlenght': 2800}))

    class Meta:
        model = Lesson
        fields = ('message',)
