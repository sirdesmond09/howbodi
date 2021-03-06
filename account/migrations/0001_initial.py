# Generated by Django 3.0 on 2020-06-25 20:18

import account.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('company_name', models.CharField(max_length=250, verbose_name='company name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('address', models.CharField(max_length=250, verbose_name='phone')),
                ('password', models.CharField(blank=True, max_length=250, verbose_name='password')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff')),
                ('is_default', models.BooleanField(blank=True, verbose_name='default')),
                ('is_hospital', models.BooleanField(blank=True, verbose_name='hospital')),
                ('is_company', models.BooleanField(blank=True, verbose_name='company')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('token', models.CharField(blank=True, max_length=300, verbose_name='token')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', account.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('token', models.CharField(blank=True, max_length=300)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
