# Generated by Django 3.2 on 2021-07-05 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_rename_course_course_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course_details',
            new_name='course',
        ),
    ]
