# Generated by Django 3.2.5 on 2021-07-10 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20210710_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='video',
        ),
    ]
