# Generated by Django 4.1.3 on 2022-11-27 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_info_student_id_result"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Result",
        ),
    ]