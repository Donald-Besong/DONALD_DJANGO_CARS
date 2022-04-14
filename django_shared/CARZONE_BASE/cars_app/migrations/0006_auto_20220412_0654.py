# Generated by Django 3.2.12 on 2022-04-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_app', '0005_auto_20220409_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='body_style',
            field=models.CharField(default='Sedan', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='Sedan', max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='interrior',
            field=models.CharField(default='Sedan', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='miles',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(default='Sedan', max_length=100),
        ),
    ]