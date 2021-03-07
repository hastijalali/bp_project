# Generated by Django 3.1.7 on 2021-03-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20210304_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='year',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='year',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(choices=[('Movies', 'Movies'), ('bp', 'bp')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='identity',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roll_no',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]