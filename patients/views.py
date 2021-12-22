from rest_framework.generics import ListAPIView

from authentication.permissions import IsDoctorUser
from .models import Patient
from .serializers import PatientListSerializer
from .constants import COUNT_OF_NEW_PATIENTS


class LastPatientsListAPIView(ListAPIView):
    """The view returns a list of recent patients."""

    permission_classes = [IsDoctorUser]
    serializer_class = PatientListSerializer

    def get_queryset(self):
        return Patient.objects.all()[:COUNT_OF_NEW_PATIENTS]
