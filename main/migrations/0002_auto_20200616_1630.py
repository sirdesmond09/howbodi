# Generated by Django 3.0 on 2020-06-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
