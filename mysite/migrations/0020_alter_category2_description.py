# Generated by Django 3.2.5 on 2021-07-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_remove_category2_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category2',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
