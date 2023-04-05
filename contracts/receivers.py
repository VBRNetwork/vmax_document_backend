from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documents
from django.conf import settings
import datetime
import os

@receiver(post_save, sender=Documents)
def send_email_receiver(sender, instance, created, **kwargs):
    if created:
        created_at = os.path.getctime("media/" + str(instance.file))
        updated_at = os.path.getmtime("media/" + str(instance.file))
        dt = datetime.datetime.fromtimestamp(created_at)
        dt1 = datetime.datetime.fromtimestamp(updated_at)
        parsed_created = str(dt).split('.')[0]
        parsed_updated = str(dt1).split('.')[0]
        
        instance.document_created_at = parsed_created
        instance.document_updated_at = parsed_updated
        instance.save()
        print("Document created at: " + str(instance.document_created_at))
        print("Document updated at: " + str(instance.document_updated_at))