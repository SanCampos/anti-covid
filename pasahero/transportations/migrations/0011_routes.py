# Generated by Django 2.2.5 on 2020-03-20 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportations', '0010_auto_20200320_0628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
    ]
