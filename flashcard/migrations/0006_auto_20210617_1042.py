# Generated by Django 2.2 on 2021-06-17 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0005_item_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='article',
        ),
    ]