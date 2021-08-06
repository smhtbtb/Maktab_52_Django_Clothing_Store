# Generated by Django 3.2.5 on 2021-08-06 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is it deleted')),
                ('name', models.CharField(help_text='Name of the brand', max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is it deleted')),
                ('name', models.CharField(help_text='Name of the category', max_length=50, verbose_name='Name')),
                ('parent', models.ForeignKey(blank=True, default=None, help_text='For example cloth have three parents. Men, Women and Children', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='product.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is it deleted')),
                ('type', models.CharField(choices=[('%', '% (Percent)'), ('$', '$ (Toomaan)')], help_text='Type of the discount (percent% or amount$)', max_length=1, verbose_name='Type')),
                ('name', models.CharField(help_text='Name of the discount', max_length=50, verbose_name='Name')),
                ('amount', models.PositiveIntegerField(help_text='Input positive amount', verbose_name='Discount Amount')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is it deleted')),
                ('creat_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='creat timestamp')),
                ('modify_timestamp', models.DateTimeField(auto_now=True, verbose_name='modify timestamp')),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True, verbose_name='delete timestamp')),
                ('name', models.CharField(help_text='Name of the product', max_length=50, verbose_name='Name')),
                ('price', models.PositiveIntegerField(help_text='Input positive amount in Toomaan/1000', verbose_name='Price')),
                ('leftovers', models.PositiveIntegerField(help_text='Input positive amount', verbose_name='Leftovers')),
                ('description', models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Description')),
                ('image', models.FileField(blank=True, default=None, help_text='Image of the product', null=True, upload_to='ProductImages/', verbose_name='Image')),
                ('color', models.CharField(help_text='Color of the product', max_length=30, verbose_name='Color')),
                ('size', models.CharField(blank=True, default=None, help_text="Size of the product (If it has'nt size, DO NOT fill it)", max_length=30, null=True, verbose_name='Size')),
                ('brand', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='product.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='product.category', verbose_name='Category')),
                ('discount', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='product.discount', verbose_name='Discount')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['category', 'creat_timestamp'],
            },
        ),
    ]
