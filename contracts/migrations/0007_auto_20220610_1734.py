# Generated by Django 3.1.5 on 2022-06-10 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_auto_20220610_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vbrcontracts',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.vbrpartners'),
        ),
    ]
