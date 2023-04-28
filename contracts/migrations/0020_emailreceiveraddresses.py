# Generated by Django 3.1.5 on 2023-04-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0019_documents_document_email_uploader'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailReceiverAddresses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email_address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Email Receiver Address',
                'verbose_name_plural': 'Email Receiver Addresses',
                'ordering': ['-id'],
            },
        ),
    ]