# Generated by Django 3.1.5 on 2022-07-10 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0009_vbrcontractssignatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='VbrDocuments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document_name', models.CharField(blank=True, max_length=255, null=True)),
                ('document_description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='vbr_documents/')),
                ('document_start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('document_end_date', models.CharField(blank=True, max_length=255, null=True)),
                ('document_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vbr_documents', to=settings.AUTH_USER_MODEL)),
                ('document_participants', models.ManyToManyField(blank=True, related_name='vbr_documents_participants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'VBR Document',
                'verbose_name_plural': 'VBR Documents',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VbrDocumentTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.ManyToManyField(blank=True, null=True, related_name='vbr_document_tags', to='contracts.VbrDocuments')),
            ],
            options={
                'verbose_name': 'VBR Document Tag',
                'verbose_name_plural': 'VBR Document Tags',
                'ordering': ['-id'],
            },
        ),
    ]
