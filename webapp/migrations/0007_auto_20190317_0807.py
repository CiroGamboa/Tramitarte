# Generated by Django 2.1.7 on 2019-03-17 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190317_0805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclesell',
            old_name='buyer',
            new_name='buyer_pic',
        ),
        migrations.RenameField(
            model_name='vehiclesell',
            old_name='seller',
            new_name='seller_pic',
        ),
    ]
