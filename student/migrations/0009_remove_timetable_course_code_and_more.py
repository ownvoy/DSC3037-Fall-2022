# Generated by Django 4.1.3 on 2022-11-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0008_remove_timetable_semester_timetable_trial_history"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timetable",
            name="course_code",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="student_id",
        ),
        migrations.AddField(
            model_name="academic",
            name="student_grade",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="preference",
            name="onlinePreference",
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="History",
        ),
        migrations.DeleteModel(
            name="Timetable",
        ),
    ]