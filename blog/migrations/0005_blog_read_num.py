# Generated by Django 2.0 on 2022-02-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220215_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]