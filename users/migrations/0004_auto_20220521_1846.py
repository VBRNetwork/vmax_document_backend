# Generated by Django 3.1.5 on 2022-05-21 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_accountsettings_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsettings',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_settings', to=settings.AUTH_USER_MODEL),
        ),
    ]
