# Generated by Django 2.1.7 on 2019-05-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0053_lessonstudent_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonstudent',
            name='total_right',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lessonstudent',
            name='total_wrong',
            field=models.IntegerField(default=0),
        ),
    ]