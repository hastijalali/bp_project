# Generated by Django 3.1.7 on 2021-03-06 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20210306_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='year',
            field=models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.course'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='teacher',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.userprofile'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(choices=[('bp', 'bp'), ('movies', 'movies')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='solution',
            name='assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.assignment'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roll_no',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
