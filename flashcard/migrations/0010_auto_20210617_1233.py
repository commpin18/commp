# Generated by Django 2.2 on 2021-06-17 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0009_auto_20210617_1203'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='ItemFC',
        ),
    ]