# Generated by Django 4.1.3 on 2022-12-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_and_time_of_publication',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
