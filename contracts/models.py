from django.db import models
from users.models import User

DOCUMENT_TYPES = (
    ("Contract", "Contract"),
    ("Pre-Contract", "Pre-Contract"),
    ("Supplier Invoice", "Supplier Invoice"),
    ("VBR Invoice", "VBR Invoice"),
    ("NDA", "NDA"),
    ("Document", "Document"),
    ("Other", "Other"),
)

class VbrPartners(models.Model):

    id = models.AutoField(primary_key=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    partner_logo = models.ImageField(
        upload_to="vbr_partners/", blank=True, null=True
    )
    partner_url = models.CharField(max_length=255, blank=True, null=True)
    partner_description = models.TextField(blank=True, null=True)
    partner_entity_name = models.CharField(
        max_length=255, blank=True, null=True
    )
    partner_administrator_name = models.CharField(
        max_length=255, blank=True, null=True
    )
    partner_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = "VBR Partner"
        verbose_name_plural = "VBR Partners"


class VbrContracts(models.Model):

    id = models.AutoField(primary_key=True)
    contract_id = models.CharField(max_length=255, blank=True, null=True)
    contract_name = models.CharField(max_length=255, blank=True, null=True)
    contract_description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="vbr_contracts/", blank=True, null=True)
    contract_start_date = models.CharField(
        max_length=255, blank=True, null=True
    )
    # partner = models.ForeignKey(VbrPartners, on_delete=models.CASCADE, blank=True, null=True)
    partner = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.contract_name}"

    class Meta:
        verbose_name = "VBR Contract"
        verbose_name_plural = "VBR Contracts"
        ordering = ["-contract_id"]

class CompanyLocations(models.Model):

    id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    location_address = models.CharField(max_length=255, blank=True, null=True)
    location_city = models.CharField(max_length=255, blank=True, null=True)
    location_zip = models.CharField(max_length=255, blank=True, null=True)
    location_country = models.CharField(max_length=255, blank=True, null=True)
    location_manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="company_locations",
    )

    def __str__(self):
        return f"NAME: {self.location_name} | CITY: {self.location_city}| MANAGER: {self.location_manager.username}"
    
class EmailReceiverAddresses(models.Model):

    id = models.AutoField(primary_key=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email_address
    
    class Meta:
        verbose_name = "Email Receiver Address"
        verbose_name_plural = "Email Receiver Addresses"
        ordering = ["-id"]


class Documents(models.Model):

    id = models.AutoField(primary_key=True)
    document_id = models.CharField(max_length=255, blank=True, null=True)
    document_attachment_id = models.CharField(
        max_length=255, blank=True, null=True
    )
    document_has_attachment = models.BooleanField(default=False)
    document_name = models.CharField(max_length=255, blank=True, null=True)
    document_description = models.TextField(blank=True, null=True)
    document_type = models.CharField(
        max_length=255, choices=DOCUMENT_TYPES, blank=True, null=True
    )
    document_extension = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey(
        CompanyLocations,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="documents",
    )
    file = models.FileField(upload_to="vbr_documents/", blank=True, null=True)
    partner = models.CharField(max_length=255, blank=True, null=True)
    document_uploader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="documents",
    )
    document_email_uploader = models.CharField(
        max_length=255, blank=True, null=True
    )
    document_upload_date = models.DateTimeField(auto_now_add=True)
    document_created_at = models.CharField(max_length=255, blank=True, null=True)
    document_updated_at = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return (
            f"""
                NAME: {self.document_name} | 
                TYPE: {self.document_type} | 
                PARTNER: {self.partner} |
                UPLOADED ON: {self.document_upload_date}
            """
        )
    
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ["-document_upload_date"]



class VbrContractsSignatures(models.Model):

    id = models.AutoField(primary_key=True)
    signature_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="vbr_contract_signatures",
    )
    contract = models.OneToOneField(
        VbrContracts,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="vbr_contract_signatures",
    )
    ##TODO: add foreign key to signature
    signature = models.ImageField(
        upload_to="vbr_contracts_signatures/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.signature_name} | {self.user.username}"

    class Meta:
        verbose_name = "VBR Contract Signature"
        verbose_name_plural = "VBR Contract Signatures"
        ordering = ["-id"]


class VbrDocuments(models.Model):

    id = models.AutoField(primary_key=True)
    document_owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="vbr_documents",
    )
    document_participants = models.ManyToManyField(
        "users.User", blank=True, related_name="vbr_documents_participants"
    )
    document_name = models.CharField(max_length=255, blank=True, null=True)
    document_description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="vbr_documents/", blank=True, null=True)
    document_start_date = models.CharField(
        max_length=255, blank=True, null=True
    )
    document_end_date = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(
        "contracts.VbrDocumentTags", blank=True, null=True
    )

    def __str__(self):
        return f"{self.document_name} | {self.document_owner.username}"

    class Meta:
        verbose_name = "VBR Document"
        verbose_name_plural = "VBR Documents"
        ordering = ["-id"]


# class VbrDocumentsFromEmail(models.Model):

#     id = models.AutoField(primary_key=True)


class VbrDocumentTags(models.Model):

    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.tag_name}"

    class Meta:
        verbose_name = "VBR Document Tag"
        verbose_name_plural = "VBR Document Tags"
        ordering = ["-id"]
