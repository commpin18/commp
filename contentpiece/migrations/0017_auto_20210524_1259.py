# Generated by Django 2.2 on 2021-05-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentpiece', '0016_auto_20210524_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=None, max_length=500),
        ),
    ]
