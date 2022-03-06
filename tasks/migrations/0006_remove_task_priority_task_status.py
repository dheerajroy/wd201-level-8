# Generated by Django 4.0.1 on 2022-03-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_priority_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=100),
        ),
    ]
