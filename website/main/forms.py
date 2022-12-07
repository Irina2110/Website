from dataclasses import fields
from .models import Task,Notes
from django.forms import ModelForm,widgets,TextInput,Textarea,DateTimeInput

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task"]
        widgets={"title":TextInput(attrs={'class':'form-control','placeholder': 'Введите название'}),
                 "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                 }

class NotesForm(ModelForm):
    class Meta:
        model=Notes
        fields=["title","full_text","date"]
        widgets= {
        "title":TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название заметки'
        }),
         "full_text" : Textarea(attrs={
             'class': 'form-control',
             'placeholder': 'Текст заметки'
        }),
         "date": DateTimeInput(attrs={
             'class':'form-control',
             'placeholder': 'Дата  добавления заметки'
         })
    }

