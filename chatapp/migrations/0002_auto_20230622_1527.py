# Generated by Django 3.2.19 on 2023-06-22 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatecontactlist',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_contact_lists_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='privatecontactlist',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_contact_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
