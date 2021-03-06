# Generated by Django 3.2 on 2021-07-05 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20210705_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_duration', models.CharField(max_length=500)),
                ('course_fee', models.TextField(max_length=1000)),
                ('course_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portal.add_course')),
                ('courser_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portal.employee')),
            ],
        ),
    ]
