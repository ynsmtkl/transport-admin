# Generated by Django 2.2 on 2019-05-03 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_bus_driver_parent_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='user_connect',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='user_connect',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]