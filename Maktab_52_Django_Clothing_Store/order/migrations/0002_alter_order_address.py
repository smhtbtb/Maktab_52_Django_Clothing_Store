# Generated by Django 3.2.5 on 2021-12-03 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.address', verbose_name='Address'),
        ),
    ]
