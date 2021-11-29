# Generated by Django 3.1.7 on 2021-11-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=100)),
            ],
        ),
    ]
