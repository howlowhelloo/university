from django.contrib import admin
from .models import Student
from .forms import StudentForm

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ('full_name', 'course', 'program', 'eta')  # Показ в таблице
    list_filter = ('course',)  # Фильтрация по курсу
    ordering = ('full_name',)  # Сортировка по алфавиту
    search_fields = ('full_name', 'program')
    
