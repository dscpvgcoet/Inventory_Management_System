# Generated by Django 3.2.4 on 2023-06-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20230630_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='total_amt',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
