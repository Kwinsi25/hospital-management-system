# Generated by Django 5.2.4 on 2025-07-19 09:05

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.models.UserManager()),
            ],
        ),
    ]
