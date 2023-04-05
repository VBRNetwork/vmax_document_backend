from django.db import models

# Create your models here.
class Signature(models.Model):
    name = models.CharField(max_length=255)
    signature = models.FileField(upload_to="signatures/")
    date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="signature"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date"]
        verbose_name = "Signature"
        verbose_name_plural = "Signatures"
