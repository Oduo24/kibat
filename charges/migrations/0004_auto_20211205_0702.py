# Generated by Django 3.1.7 on 2021-12-05 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charges', '0003_auto_20211205_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charges',
            old_name='customer',
            new_name='tenant',
        ),
    ]