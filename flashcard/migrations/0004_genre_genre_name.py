# Generated by Django 2.2 on 2021-06-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0003_auto_20210617_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(default='Image', max_length=100),
        ),
    ]
