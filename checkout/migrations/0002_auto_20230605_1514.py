# Generated by Django 3.2.18 on 2023-06-05 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address2',
            new_name='address2',
        ),
    ]
