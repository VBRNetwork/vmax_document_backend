# Generated by Django 3.1.5 on 2022-08-19 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_customers'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='appointment_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customers'),
        ),
    ]
