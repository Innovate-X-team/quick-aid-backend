# Generated by Django 5.1.1 on 2024-10-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_task_task_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='provideruser',
            name='on_work',
            field=models.BooleanField(default=False),
        ),
    ]