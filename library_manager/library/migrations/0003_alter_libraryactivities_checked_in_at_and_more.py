# Generated by Django 4.0.1 on 2022-01-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_isbn_name_books_isbn_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryactivities',
            name='checked_in_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='libraryactivities',
            name='checked_out_at',
            field=models.DateTimeField(null=True),
        ),
    ]
