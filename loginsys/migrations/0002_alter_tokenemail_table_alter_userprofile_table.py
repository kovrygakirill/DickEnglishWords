# Generated by Django 4.0 on 2022-12-21 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tokenemail',
            table='token_email',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='user_profile',
        ),
    ]
