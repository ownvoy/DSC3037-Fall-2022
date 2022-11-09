from django.db import models


class Subject(models.Model):
    degree_courses = models.CharField(max_length=100)
    type_of_field3 = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    course_title_english = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    campus = models.CharField(max_length=100)
    type_of_field2= models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    classtime = models.CharField(max_length=100)
    type_of_class1 = models.CharField(max_length=100)
    type_of_class2 = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
