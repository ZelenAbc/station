# Generated by Django 2.0.1 on 2018-01-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='text',
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
