# Generated by Django 5.1.1 on 2024-09-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
