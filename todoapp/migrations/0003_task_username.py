# Generated by Django 4.1.3 on 2023-04-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='username',
            field=models.CharField(default='js', max_length=200, unique=True),
        ),
    ]
