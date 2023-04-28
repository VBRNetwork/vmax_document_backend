from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EmployeesLeaves
from django.conf import settings
from .utils import new_email_sender

@receiver(post_save, sender=EmployeesLeaves)
def send_email_receiver(sender, instance, created, **kwargs):
    if created:
        new_email_sender(
            send_to=settings.EMAIL_SEND_TO,
            subject=f"[CERERE ANGAJAT] - {instance.user.first_name} {instance.user.last_name} {instance.leave_type.name}",
            message=
            f"""
                <div>
                    <h3>Hello,<h3/> 
                    <p style='font-weight:400;'>
                        You have a new request for {instance.leave_type.name} 
                        from {instance.user.first_name} 
                        {instance.user.last_name} 
                        from {instance.start_date} 
                        to {instance.end_date}.
                    </p>
                </div>
            """,
        )
    print("SLOBOZESCU:", "Email sent successfully")