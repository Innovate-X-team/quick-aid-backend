# Generated by Django 5.1.1 on 2024-10-18 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_provideruser_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='provideruser',
            name='city',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provideruser',
            name='reg_no',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provideruser',
            name='state',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]