# Generated by Django 2.1.7 on 2019-03-20 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='ans',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='mac_address',
            new_name='mac',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='student',
            new_name='nmec',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='execution_date',
            new_name='start_date',
        ),
    ]