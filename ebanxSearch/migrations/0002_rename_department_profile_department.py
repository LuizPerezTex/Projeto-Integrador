# Generated by Django 4.0.6 on 2022-08-15 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebanxSearch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='department',
            new_name='Department',
        ),
    ]
