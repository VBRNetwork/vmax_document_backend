# Generated by Django 3.1.5 on 2022-06-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_auto_20220609_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vbrcontracts',
            name='partner',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]