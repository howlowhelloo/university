from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Student
from .forms import StudentForm

def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/add_student.html', {'form': form})

def student_list(request):
    query = request.GET.get('q')
    course = request.GET.get('course')
    sort = request.GET.get('sort', 'asc')

    students = Student.objects.all()

    if query:
        students = students.filter(full_name__icontains=query)

    if course:
        students = students.filter(course=course)

    if sort == 'desc':
        students = students.order_by('-full_name')
    else:
        students = students.order_by('full_name')

    total_students = students.count()

    course_stats = (
        Student.objects.values('course')
        .annotate(count=Count('id'))
        .order_by('course')
    )

    return render(request, 'students/student_list.html', {
        'students': students,
        'total_students': total_students,
        'current_sort': sort,
        'course_stats': course_stats,
        'query': query,
    })
def app2_page(request):
    return render(request, 'app2/me.html')