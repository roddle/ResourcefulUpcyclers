# Generated by Django 2.0.1 on 2018-04-26 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180424_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='bio',
            new_name='description',
        ),
    ]
