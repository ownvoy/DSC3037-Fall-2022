# Generated by Django 4.1.3 on 2022-11-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0003_academic_student_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academic",
            name="double_major",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="academic",
            name="student_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="academic",
            name="triple_major",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]