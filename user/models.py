from django.db import models

from skku.models import Subject
from student.models import Academic


class Info(models.Model):
    student_id = models.ForeignKey(Academic, on_delete=models.CASCADE, primary_key=True, unique=True,
                                   db_column='student_id')
    login_id = models.CharField(max_length=20)
    login_password = models.CharField(max_length=20)

# Create your models here.
