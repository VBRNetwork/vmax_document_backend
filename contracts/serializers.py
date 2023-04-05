from rest_framework import serializers
from .models import (
    VbrContracts,
    VbrDocuments,
    VbrPartners,
    Documents,
    CompanyLocations,
)
from users.serializers import UserSerializer
from dry_rest_permissions.generics import DRYPermissionsField
from .utils import convert_doc_to_pdf
import uuid



class VbrPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = VbrPartners
        fields = "__all__"


class VbrDocumentsSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)

    def validate(self, data):
        validated = super().validate(data)

        file = validated.get("file")
        file_name = file.name
        ext = file_name.split(".")[-1]

        if ext not in ["docx", "doc", "pdf", "xlsx", "xls"]:
            raise serializers.ValidationError(
                "File must be .docx, .doc or .pdf or .xlsx or .xls"
            )

        return validated

    class Meta:
        model = VbrDocuments
        fields = "__all__"

class CompanyLocationsSerializer(serializers.ModelSerializer):
    location_manager = UserSerializer(read_only=True)
    class Meta:
        model = CompanyLocations
        fields = (
            "id",
            "location_name",
            "location_address",
            "location_city",
            "location_zip",
            "location_country",
            "location_manager",
        )

class DocumentsSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    document_uploader = UserSerializer(read_only=True)
    location = CompanyLocationsSerializer(read_only=True)
    
    def validate(self, data):
        validated_data = super().validate(data)

        file = validated_data.get("file")
        file_name = file.name
        ext = file_name.split(".")[-1]
     
        document_id = uuid.uuid4()


        if ext not in ["docx", "doc", "pdf", "xlsx", "xls"]:
            raise serializers.ValidationError(
                "File must be .docx, .doc or .pdf or .xlsx or .xls"
            )
        # if ext in ["docx", "doc"]:
        #     file = convert_doc_to_pdf(file=file)
        #     validated_data["file"] = file
        #     ext = "pdf"

        validated_data["document_uploader"] = self.context["request"].user
        validated_data["document_name"] = file_name.split(".")[0]
        validated_data["document_extension"] = ext.upper()
        validated_data["document_id"] = document_id


        return validated_data

    class Meta:
        model = Documents
        fields = (
            "id",
            "file",
            "document_type",
            "document_name",
            "document_description",
            "document_id",
            "document_uploader",
            "document_upload_date",
            "document_created_at",
            "document_updated_at",
            "partner",
            "location",
            "document_extension",
            "document_attachment_id",
            "document_has_attachment",
            "document_email_uploader",

        )


class VbrContractsSerializer(serializers.ModelSerializer):
    # partner = VbrPartnersSerializer(many=False)
    file = serializers.FileField(required=True)

    def validate(self, data):
        validated = super().validate(data)

        file = validated.get("file")
        file_name = file.name
        ext = file_name.split(".")[-1]

        if ext not in ["docx", "doc", "pdf"]:
            raise serializers.ValidationError(
                "File must be .docx, .doc or .pdf"
            )

        if ext in ["docx", "doc"]:
            file = convert_doc_to_pdf(file=file)
            validated["file"] = file.read()

        return validated

    class Meta:
        model = VbrContracts
        fields = "__all__"
