# Generated by Django 3.2.23 on 2024-01-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('salt', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('failed_login_tries', models.SmallIntegerField(default=0)),
            ],
        ),
    ]