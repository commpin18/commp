# Generated by Django 2.2 on 2021-05-22 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentpiece', '0010_item_favourites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='favourites',
            new_name='favourite',
        ),
    ]
