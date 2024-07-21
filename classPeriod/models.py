from django.db import models
from teacher.models import Teacher

# Create your models here.
class ClassPeriod(models.Model):
    
    teacher_first_name = models.ManyToManyField(Teacher)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length = 20)
    classroom = models.CharField(max_length = 20)
    date_of_the_week = models.DateField()

    def __str__(self):
        return f"{self.start_time} {self.end_time}"
