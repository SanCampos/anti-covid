# Generated by Django 2.2.5 on 2020-03-20 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commuters', '0005_commuters_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commuters',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commuter', to=settings.AUTH_USER_MODEL),
        ),
    ]
