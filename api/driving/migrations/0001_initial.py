# Generated by Django 2.2 on 2019-05-03 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20190503_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('user_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserConnect')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cne', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driving.Parent')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(max_length=10)),
                ('date_licence', models.DateField()),
                ('user_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserConnect')),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_place', models.IntegerField()),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='driving.Driver')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driving.Parent')),
            ],
        ),
    ]
