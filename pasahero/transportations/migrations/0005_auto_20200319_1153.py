# Generated by Django 2.2.5 on 2020-03-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportations', '0004_transportations_road'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportations',
            name='road',
            field=models.CharField(max_length=128),
        ),
    ]
