# Generated by Django 3.2.1 on 2021-05-04 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0009_joke_joke_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joke',
            name='created_at',
        ),
    ]