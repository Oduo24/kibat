# Generated by Django 3.1.7 on 2021-12-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charges', '0005_auto_20211205_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='charges',
            name='unit',
            field=models.CharField(default='UNIT ID', max_length=30),
            preserve_default=False,
        ),
    ]
