# Generated by Django 4.1.3 on 2022-11-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='profile_picture',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
