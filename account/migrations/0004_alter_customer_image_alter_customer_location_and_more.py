# Generated by Django 4.0.1 on 2022-05-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_createcustomer_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='avatar/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
