# Generated by Django 4.1.3 on 2022-11-17 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("skku", "0005_remove_subject_id_subject_course_id"),
        ("student", "0010_history"),
        ("user", "0002_rename_user_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="student_id",
            field=models.ForeignKey(
                db_column="student_id",
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="student.academic",
                unique=True,
            ),
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                ("result_id", models.AutoField(primary_key=True, serialize=False)),
                ("trial", models.IntegerField()),
                (
                    "course_id",
                    models.ForeignKey(
                        db_column="course_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skku.subject",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        db_column="student_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student.academic",
                    ),
                ),
            ],
        ),
    ]