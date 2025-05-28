from django.urls import path
from .views import add_student, student_list

urlpatterns = [
    path('add/', add_student, name='add_student'),
    path('list/', student_list, name='student_list'),
]
