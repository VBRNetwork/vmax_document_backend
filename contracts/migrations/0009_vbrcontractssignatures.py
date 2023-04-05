# Generated by Django 3.1.5 on 2022-07-10 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0008_auto_20220705_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='VbrContractsSignatures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('signature_name', models.CharField(blank=True, max_length=255, null=True)),
                ('signature', models.ImageField(blank=True, null=True, upload_to='vbr_contracts_signatures/')),
                ('contract', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vbr_contract_signatures', to='contracts.vbrcontracts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vbr_contract_signatures', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'VBR Contract Signature',
                'verbose_name_plural': 'VBR Contract Signatures',
                'ordering': ['-id'],
            },
        ),
    ]
