# Generated by Django 3.0 on 2020-07-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_member_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('assessment_taken', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=300)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_individual',
        ),
    ]