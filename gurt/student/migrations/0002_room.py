# Generated by Django 2.2.6 on 2019-10-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=30)),
                ('Name_Student', models.CharField(max_length=30)),
                ('Last_nameStudent', models.CharField(max_length=30)),
            ],
        ),
    ]
