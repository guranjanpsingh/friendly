# Generated by Django 2.0.2 on 2018-03-04 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendly_api', '0002_userlocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlocation',
            old_name='last_update',
            new_name='last_updated',
        ),
    ]