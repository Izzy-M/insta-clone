# Generated by Django 3.1.7 on 2021-09-17 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='photo',
            new_name='post',
        ),
    ]
