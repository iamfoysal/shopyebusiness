# Generated by Django 4.0.1 on 2022-05-24 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createcustomer',
            old_name='User',
            new_name='user',
        ),
    ]
