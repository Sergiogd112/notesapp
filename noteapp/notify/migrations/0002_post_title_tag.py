# Generated by Django 3.1.1 on 2020-09-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=models.CharField(max_length=255), max_length=255),
        ),
    ]
