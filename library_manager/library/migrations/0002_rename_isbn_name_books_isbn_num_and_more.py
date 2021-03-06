# Generated by Django 4.0.1 on 2022-01-10 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='isbn_name',
            new_name='isbn_num',
        ),
        migrations.AlterField(
            model_name='librarybooks',
            name='last_library_activity_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.libraryactivities'),
        ),
    ]
