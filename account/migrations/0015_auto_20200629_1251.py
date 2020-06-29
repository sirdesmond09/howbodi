# Generated by Django 3.0 on 2020-06-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200627_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
        migrations.AddField(
            model_name='user',
            name='cac_reg_no',
            field=models.CharField(default='34d4r', max_length=50, verbose_name='Registration number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='industry',
            field=models.CharField(max_length=250, null=True, verbose_name='industry'),
        ),
        migrations.AddField(
            model_name='user',
            name='local_gov',
            field=models.CharField(max_length=250, null=True, verbose_name='local government'),
        ),
        migrations.AddField(
            model_name='user',
            name='staff_pop',
            field=models.IntegerField(default=44, verbose_name='staff population'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=250, null=True, verbose_name='state'),
        ),
    ]
