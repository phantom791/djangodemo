# Generated by Django 2.0.7 on 2020-04-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=120)),
                ('course_instructor', models.CharField(max_length=120)),
                ('course_duration', models.DurationField(null=True)),
                ('course_start_time', models.TimeField(null=True)),
            ],
        ),
    ]
