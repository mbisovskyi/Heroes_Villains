# Generated by Django 4.0.6 on 2022-07-18 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_power_remove_super_primary_ability_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='primary_ability',
        ),
        migrations.RemoveField(
            model_name='super',
            name='secondary_ability',
        ),
        migrations.AddField(
            model_name='super',
            name='powers',
            field=models.ManyToManyField(to='supers.power'),
        ),
    ]
