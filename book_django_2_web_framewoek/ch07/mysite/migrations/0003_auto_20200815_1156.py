# Generated by Django 2.0 on 2020-08-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20200815_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pphoto',
            name='url',
            field=models.URLField(default='https://i.imgur.com/TQTfGiA.jpg'),
        ),
    ]