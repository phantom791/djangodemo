# Generated by Django 2.0.7 on 2020-03-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
