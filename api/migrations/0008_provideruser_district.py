# Generated by Django 5.1.1 on 2024-10-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_provideruser_current_lat_provideruser_current_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='provideruser',
            name='district',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
