# Generated by Django 4.2 on 2023-04-14 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_asset_returned_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
