# Generated by Django 3.2 on 2021-05-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0008_joke_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='joke_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
