# Generated by Django 3.1.5 on 2022-05-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220521_1902'),
    ]

    operations = [
        migrations.AlterField('AccountSettings', 'price_column', models.CharField(max_length=50, blank=True, null=True)),
    ]
