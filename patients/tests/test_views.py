import factory
from django.urls import reverse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.tests.factories import UserFactory, ProfileFactory
from patients.tests.factories import PatientFactory, DiagnoseFactory
from patients.views import LastPatientsListAPIView


class LastPatientsListAPIViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        non_doctor = ProfileFactory()
        doctor = ProfileFactory(is_doctor=True)
        diagnoses = DiagnoseFactory.create_batch(3)

        cls.url = reverse('patients:last_patients_list')
        cls.auth_url = reverse('authentication:token_obtain_pair')
        cls.non_doctor = non_doctor
        cls.doctor = doctor
        cls.view = LastPatientsListAPIView.as_view()
        cls.patients = PatientFactory.create_batch(5, diagnoses=diagnoses)

    def test_patients_list_for_doctor_GET(self):
        data = {
            'username': self.doctor.user.username,
            'password': '1234',
        }
        auth_response = self.client.post(self.auth_url, data=data, format='json')
        token = auth_response.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.url)

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(3, len(response.data))
        self.assertEquals(self.view.__name__, response.resolver_match.func.__name__)

    def test_patients_list_for_user_GET(self):
        data = {
            'username': self.non_doctor.user.username,
            'password': '1234',
        }
        auth_response = self.client.post(self.auth_url, data=data, format='json')
        token = auth_response.data.get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.url)
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_patients_list_without_auth_GET(self):
        response = self.client.get(self.url)
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)