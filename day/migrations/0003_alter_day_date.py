# Generated by Django 4.0.5 on 2022-06-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0002_day_date_day_shifts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(null=True),
        ),
    ]