from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.views import CustomTokenObtainPairView

from .factories import UserFactory


class CustomTokenObtainPairViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('authentication:token_obtain_pair')
        cls.user = UserFactory()
        cls.password = '1234'
        cls.view = CustomTokenObtainPairView().as_view()

    def test_auth_POST(self):
        data = {
            "username":  self.user.username,
            "password": self.password,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(self.view.__name__, response.resolver_match.func.__name__)

    def test_auth_with_wrong_credentials_POST(self):
        data = {
            "username":  self.user.username,
            "password": 'bad_pass',
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_auth_without_credentials_POST(self):
        response = self.client.post(self.url, data={}, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
