# Generated by Django 2.1.7 on 2019-03-10 02:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='date_posted',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='quiz',
            name='course',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
