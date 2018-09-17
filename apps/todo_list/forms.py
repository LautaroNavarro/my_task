from django import forms
from apps.todo_list.models import Priority, Estate, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'name', 'description', 'priority', 'estate'}
        labels = {'name': 'Name',
                  'description': 'Description',
                  'priority': 'Priority',
                  'estate': 'Estate',
                  }
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   'priority': forms.Select(attrs = {'class' : 'form-control'} ,choices = Priority.objects.all()),
                   'estate': forms.Select(attrs = {'class' : 'form-control'} ,choices = Estate.objects.all()),
                   }
