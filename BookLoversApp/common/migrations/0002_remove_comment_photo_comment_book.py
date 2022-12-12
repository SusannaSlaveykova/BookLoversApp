# Generated by Django 4.1.3 on 2022-11-29 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='books.book'),
            preserve_default=False,
        ),
    ]