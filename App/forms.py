from django import forms
from App.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nickname', 'feedback']
        labels = {
            'nickname': 'Ник',
            'feedback': 'Отзыв'
        }

