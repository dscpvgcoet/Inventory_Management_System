# Generated by Django 3.2.4 on 2023-06-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20230630_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='sale',
            name='qty',
            field=models.FloatField(default=0),
        ),
    ]
