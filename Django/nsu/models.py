from django.db import models
from django.shortcuts import redirect


class University(models.Model):
    full_title = models.CharField('Полное название', max_length=125)
    small_title = models.CharField('Сокращенное название', max_length=15)
    date = models.DateField('Дата создания')

    def __str__(self):
        return self.small_title

    def get_absolute_url(self):
        return '/univer'

    class Meta:
        verbose_name = "Универ"
        verbose_name_plural = "Все универы"


class Student(models.Model):
    name = models.CharField('ФИО', max_length=125)
    birthday = models.DateField('Дата рождения')
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    year = models.IntegerField('Год поступления')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/student'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
