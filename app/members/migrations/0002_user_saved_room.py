# Generated by Django 2.1.3 on 2018-11-28 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='saved_room',
            field=models.ManyToManyField(to='home.Room'),
        ),
    ]
