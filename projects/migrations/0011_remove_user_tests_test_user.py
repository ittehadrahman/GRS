# Generated by Django 5.0.1 on 2024-01-15 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_remove_user_test_user_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tests',
        ),
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.user'),
        ),
    ]
