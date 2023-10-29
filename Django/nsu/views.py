from django.shortcuts import render, redirect
from nsu.models import University, Student
from .forms import UniversityForm, StudentForm
from django.views.generic import UpdateView, DeleteView


class RefactorUniversity(UpdateView):
    model = University
    template_name = 'nsu/edit/edit_university.html'
    form_class = UniversityForm


class DeleteUniversity(DeleteView):
    model = University
    success_url = '/univer'
    template_name = 'nsu/delete/delete_university.html'


class RefactorStudent(UpdateView):
    model = Student
    template_name = 'nsu/edit/edit_student.html'
    form_class = StudentForm


class DeleteStudent(DeleteView):
    model = Student
    success_url = '/student'
    template_name = 'nsu/delete/delete_student.html'


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'nsu/index.html', data)


def history_university(request):
    all_obj = University.objects.order_by('full_title')
    data = {
        'title': 'Университеты',
        'list': all_obj
    }
    return render(request, 'nsu/history/university_history.html', data)


def history_students(request):
    all_obj = Student.objects.order_by('name')
    data = {
        'title': 'Студенты',
        'list': all_obj
    }
    return render(request, 'nsu/history/students_history.html', data)


def add_university(request):
    error = ''
    form = UniversityForm()
    if request.method == 'POST':
        form = UniversityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_university')
        else:
            error = 'Введите корректные данные'
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'nsu/add/add_university.html', data)


def add_student(request):
    error_student = ''
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_student')
        else:
            error_student = 'Введите корректные данные'
    data = {
        'form': form,
        'error': error_student
    }
    return render(request, 'nsu/add/add_student.html', data)


