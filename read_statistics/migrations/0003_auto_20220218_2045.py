# Generated by Django 2.0 on 2022-02-18 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0002_readdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readdetail',
            old_name='data',
            new_name='date',
        ),
    ]