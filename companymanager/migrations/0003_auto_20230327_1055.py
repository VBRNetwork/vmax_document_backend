# Generated by Django 3.1.5 on 2023-03-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companymanager', '0002_auto_20230327_0936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teams',
            options={'get_latest_by': 'created_at', 'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.AddField(
            model_name='teammembers',
            name='organizational_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
