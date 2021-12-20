from rest_framework import serializers

from .models import Patient


class PatientListSerializer(serializers.ModelSerializer):
    diagnoses = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'date_of_birth', 'diagnoses', 'created_at']
