# Generated by Django 4.1.3 on 2022-11-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_appuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]