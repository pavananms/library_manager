# Generated by Django 4.0.1 on 2022-01-13 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_libraryactivities_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libraryactivities',
            old_name='library_book_id',
            new_name='library_book',
        ),
        migrations.RenameField(
            model_name='libraryactivities',
            old_name='user_id',
            new_name='user',
        ),
    ]
