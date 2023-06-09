# Generated by Django 3.1.5 on 2022-08-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_title', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment_description', models.TextField(blank=True, null=True)),
                ('appointment_date', models.CharField(blank=True, max_length=500, null=True)),
                ('appointment_duration', models.CharField(blank=True, max_length=500, null=True)),
                ('appointment_room', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.AddIndex(
            model_name='appointments',
            index=models.Index(fields=['appointment_title'], name='appointment_appoint_70eb59_idx'),
        ),
        migrations.AddIndex(
            model_name='appointments',
            index=models.Index(fields=['id'], name='appointment_id_b8ff13_idx'),
        ),
    ]
