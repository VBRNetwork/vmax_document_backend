# Generated by Django 3.1.5 on 2023-03-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tenure',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]