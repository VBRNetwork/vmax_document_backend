# Generated by Django 3.1.5 on 2022-06-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_auto_20220609_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vbrcontracts',
            name='contract_start_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]