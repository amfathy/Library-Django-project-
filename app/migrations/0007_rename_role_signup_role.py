# Generated by Django 3.2.5 on 2021-07-16 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_signup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='Role',
            new_name='role',
        ),
    ]
