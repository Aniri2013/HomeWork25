# Generated by Django 2.2.6 on 2019-10-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Number_room', models.CharField(max_length=30)),
                ('Facultet', models.CharField(max_length=120)),
                ('Course', models.CharField(max_length=10)),
            ],
        ),
    ]
