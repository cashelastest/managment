# Generated by Django 5.1.1 on 2024-09-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connector',
            name='isFinish',
            field=models.BooleanField(default=False),
        ),
    ]