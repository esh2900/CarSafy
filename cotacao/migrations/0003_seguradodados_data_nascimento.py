# Generated by Django 2.1 on 2018-09-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0002_auto_20180923_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguradodados',
            name='data_nascimento',
            field=models.DateField(default='2018-01-01'),
            preserve_default=False,
        ),
    ]
