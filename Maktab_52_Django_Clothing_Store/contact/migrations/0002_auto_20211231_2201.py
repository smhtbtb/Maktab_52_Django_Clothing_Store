# Generated by Django 3.2.5 on 2021-12-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(help_text='Write your message here', verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(help_text='Tell me what your message is about', max_length=150, verbose_name='Subject'),
        ),
    ]
