# Generated by Django 3.1.5 on 2023-02-25 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0011_auto_20220716_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document_id', models.CharField(blank=True, max_length=255, null=True)),
                ('document_name', models.CharField(blank=True, max_length=255, null=True)),
                ('document_description', models.TextField(blank=True, null=True)),
                ('document_type', models.CharField(blank=True, choices=[('Contract', 'Contract'), ('Pre-Contract', 'Pre-Contract'), ('Supplier Invoice', 'Supplier Invoice'), ('VBR Invoice', 'VBR Invoice'), ('NDA', 'NDA'), ('Document', 'Document'), ('Other', 'Other')], max_length=255, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='vbr_documents/')),
                ('document_upload_date', models.DateTimeField(auto_now_add=True)),
                ('document_created_at', models.CharField(blank=True, max_length=255, null=True)),
                ('document_updated_at', models.CharField(blank=True, max_length=255, null=True)),
                ('document_uploader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'VBR Document',
                'verbose_name_plural': 'VBR Documents',
                'ordering': ['-document_upload_date'],
            },
        ),
    ]