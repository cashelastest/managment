# Generated by Django 5.1.1 on 2024-09-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
    ]
