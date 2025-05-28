from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    COURSE_CHOICES = [(i, f"{i} курс") for i in range(1, 6)]

    course = forms.ChoiceField(choices=COURSE_CHOICES, label="Курс")

    class Meta:
        model = Student
        fields = ['full_name', 'course', 'program']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Введите ФИ'}),
            'program': forms.TextInput(attrs={'placeholder': 'Направление обучения'}),
        }
        help_texts = {
            'course': 'Выберите курс от 1 до 5.',
        }

    def clean_course(self):
        value = int(self.cleaned_data['course'])
        if value < 1 or value > 5:
            raise forms.ValidationError("Курс должен быть от 1 до 5.")
        return value