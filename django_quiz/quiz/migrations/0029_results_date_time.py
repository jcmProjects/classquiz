# Generated by Django 2.1.7 on 2019-03-23 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0028_auto_20190323_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
