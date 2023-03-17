from django import forms
from .models import Task, ImageTask
from datetime import datetime
from django.core.validators import ValidationError
from django.utils import timezone


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'date',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'description', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'placeholder': 'date', 'class': 'form-control'}),
        }
        labels = {
            'name': '',
            'description': '',
            'date': '',
        }

    def clean_date(self):
        task_date = self.cleaned_data['date']
        now_date = datetime.now().date()
        if task_date < now_date:
            raise ValidationError('Date cannot be for the past')
        return task_date


class AddImageToTaskForm(forms.ModelForm):
    class Meta:
        model = ImageTask
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'multiple': True})
        }
