from .models import University, Student
from django.forms import ModelForm
from django import forms
from datetime import date


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ['full_title', 'small_title', 'date']

        widgets = {
            "full_title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полное название университета'
            }),
            "small_title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сокращенное название университета'
            }),
            "date": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата основания',
                'autocomplete': "off",
                'value': date.today().strftime('%d.%m.%Y')
            })
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'birthday', 'university', 'year']

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя студента'
            }),
            "birthday": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'autocomplete': "off",
                'value': date.today().strftime('%d.%m.%Y')
            }),
            "year": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год поступления'
            }),
        }
