# Generated by Django 2.2.7 on 2019-12-05 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20191204_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='clientefixo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
