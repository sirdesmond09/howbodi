# Generated by Django 3.0 on 2020-06-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200625_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(default=False, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_hospital',
            field=models.BooleanField(default=False, verbose_name='hospital'),
        ),
    ]