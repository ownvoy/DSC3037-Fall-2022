# Generated by Django 4.1.3 on 2022-11-16 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("skku", "0002_alter_subject_campus_alter_subject_classtime_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="subject",
            unique_together={("course_code", "semester", "major")},
        ),
    ]
