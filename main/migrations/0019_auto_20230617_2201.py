# Generated by Django 3.2.4 on 2023-06-17 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_franchisee_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name_plural': '4. Purchases'},
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.vendor'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Franchisee',
        ),
    ]
