# Generated by Django 3.2.19 on 2023-06-03 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0010_privatecontactlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatecontactlist',
            name='slug',
        ),
    ]
