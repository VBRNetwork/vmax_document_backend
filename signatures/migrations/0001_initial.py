# Generated by Django 3.1.5 on 2022-08-08 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('signature', models.FileField(upload_to='signatures/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='signature', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Signature',
                'verbose_name_plural': 'Signatures',
                'ordering': ['-date'],
            },
        ),
    ]
