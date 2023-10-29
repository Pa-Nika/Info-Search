from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('univer/', views.history_university, name='univer_history'),
    path('student/', views.history_students, name='student_history'),
    path('add/univer/', views.add_university, name='add_university'),
    path('add/student/', views.add_student, name='add_student'),

    path('university/edit/<int:pk>', views.RefactorUniversity.as_view(), name='edit_university'),
    path('university/delete/<int:pk>', views.DeleteUniversity.as_view(), name='delete_university'),

    path('student/edit/<int:pk>', views.RefactorStudent.as_view(), name='edit_student'),
    path('student/delete/<int:pk>', views.DeleteStudent.as_view(), name='delete_student')
]
