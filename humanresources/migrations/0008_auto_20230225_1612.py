# Generated by Django 3.1.5 on 2023-02-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humanresources', '0007_recruitmentleads_recruitment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentleads',
            name='recruitment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255),
        ),
    ]
