# Generated by Django 3.2 on 2021-05-02 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0006_joke_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joke',
            name='created_at',
        ),
    ]