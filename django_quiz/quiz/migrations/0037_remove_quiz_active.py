# Generated by Django 2.1.7 on 2019-04-03 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0036_quiz_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='active',
        ),
    ]
