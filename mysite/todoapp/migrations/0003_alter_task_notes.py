# Generated by Django 4.0.3 on 2022-03-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notes',
            field=models.TextField(default=None, null=True),
        ),
    ]
