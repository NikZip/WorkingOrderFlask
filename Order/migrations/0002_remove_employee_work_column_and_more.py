# Generated by Django 4.2.1 on 2023-05-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='work_column',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='work_shift',
        ),
        migrations.AlterField(
            model_name='transport',
            name='state_car_n',
            field=models.CharField(max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='workingorder',
            name='arrival_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workingorder',
            name='departure_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
