# Generated by Django 3.1.5 on 2023-02-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0014_documents_document_extension'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documents',
            options={'ordering': ['-document_upload_date'], 'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
    ]