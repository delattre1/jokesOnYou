# Generated by Django 3.2 on 2021-05-02 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0003_remove_joke_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
