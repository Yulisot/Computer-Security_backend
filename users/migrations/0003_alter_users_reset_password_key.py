# Generated by Django 5.0.2 on 2024-02-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_reset_password_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='reset_password_key',
            field=models.CharField(default='', max_length=100),
        ),
    ]
