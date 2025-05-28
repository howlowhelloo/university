from django.db import models
from django.core.validators import MaxValueValidator

class Student(models.Model):
    full_name = models.CharField("Фамилия и имя", max_length=100)
    course = models.PositiveIntegerField("Курс", validators=[MaxValueValidator(5)])
    program = models.CharField("Программа", max_length=100)

    class Meta:
        ordering = ['full_name']  # ← сортировка по умолчанию

    @property
    def eta(self):
        return max(0, 4 - self.course)

    def __str__(self):
        return self.full_name
    
    

    
