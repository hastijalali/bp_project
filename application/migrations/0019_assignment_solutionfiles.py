# Generated by Django 3.1.7 on 2021-03-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_solution_questionfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='solutionfiles',
            field=models.FileField(default='', upload_to='medias/solutions'),
        ),
    ]