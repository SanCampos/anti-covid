# Generated by Django 2.2.5 on 2020-03-20 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportations', '0015_auto_20200320_0644'),
        ('commuters', '0002_allowed_routes'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='allowed_routes',
            unique_together={('route_id', 'commuter_id')},
        ),
    ]
