# Generated by Django 5.0.1 on 2024-01-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_remove_user_test_user_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='test',
        ),
        migrations.AddField(
            model_name='user',
            name='tests',
            field=models.ManyToManyField(blank=True, to='projects.test'),
        ),
    ]
