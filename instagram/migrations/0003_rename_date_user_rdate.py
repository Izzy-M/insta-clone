# Generated by Django 3.2.7 on 2021-09-14 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date',
            new_name='rdate',
        ),
    ]
