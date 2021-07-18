# Generated by Django 3.2 on 2021-07-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=1000)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
    ]