# Generated by Django 3.2.12 on 2022-04-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_app', '0003_auto_20220409_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='condition',
            field=models.CharField(default='Good', max_length=100),
        ),
    ]
