# Generated by Django 2.0.1 on 2018-02-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_auto_20180220_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
