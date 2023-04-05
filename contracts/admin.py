from django.contrib import admin
from .models import (
    VbrPartners,
    VbrContracts,
    VbrContractsSignatures,
    VbrDocuments,
    VbrDocumentTags,
    Documents,
    CompanyLocations,
)

admin.site.register(VbrPartners)
admin.site.register(VbrContracts)
admin.site.register(VbrContractsSignatures)
admin.site.register(VbrDocuments)
admin.site.register(VbrDocumentTags)
admin.site.register(Documents)
admin.site.register(CompanyLocations)
