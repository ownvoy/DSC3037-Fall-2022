from django.db import models


class Subject(models.Model):
    course_id = models.AutoField(primary_key = True)
    semester = models.CharField(max_length=100)
    college = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True)
    degree_courses = models.CharField(max_length=100, null=True)
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    course_title_english = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    classtime = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100, null=True)
    campus = models.CharField(max_length=100, null=True)
    type_of_field2= models.CharField(max_length=100, null=True)
    type_of_field3 = models.CharField(max_length=100, null=True)
    type_of_class1 = models.CharField(max_length=100, null=True)
    type_of_class2 = models.CharField(max_length=100, null=True)
    remarks = models.CharField(max_length=100, null=True)


    class Meta:
        unique_together = ('course_code','semester','major')

    def __str__(self):
        return self.name
# Create your models here.
