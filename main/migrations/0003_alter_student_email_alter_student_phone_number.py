# Generated by Django 4.1.7 on 2023-03-22 18:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_student_address_student_email_student_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.CharField(
                max_length=15,
                null=True,
                validators=[
                    django.core.validators.EmailValidator("Enter a valid email")
                ],
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
