from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from users.models import User
from .models import PayrollManagement

@receiver(post_save, sender=User)
def create_payroll_receiver(sender, instance, created, **kwargs):
    if created:
        try:
            PayrollManagement.objects.create(
            payroll_user=instance,
            payroll_name=instance.username,
        )
            return JsonResponse({"message": "Payroll created successfully"}, status=201)
        except:
            return JsonResponse({"message": "Payroll not created"}, status=400)


            
