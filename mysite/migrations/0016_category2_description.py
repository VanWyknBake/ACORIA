# Generated by Django 3.2.5 on 2021-07-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_auto_20210710_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='category2',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
