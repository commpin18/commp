# Generated by Django 2.2 on 2021-05-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentpiece', '0019_auto_20210530_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='language_of_instruction',
            field=models.CharField(max_length=100),
        ),
    ]
