# Generated by Django 3.0 on 2020-06-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200625_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_individual',
            field=models.BooleanField(default=False, verbose_name='individual'),
        ),
    ]
