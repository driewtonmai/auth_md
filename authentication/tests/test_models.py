from django.contrib.auth.models import User

from django.test import TestCase

from .factories import ProfileFactory
from ..models import Profile


class ProfileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.profile = ProfileFactory(is_doctor=True)

    def test_representation_to_string(self):
        expected_str = f'Profile for user {self.profile.user.username}'
        self.assertEquals(self.profile.__str__(), expected_str)

    def test_signal_create_or_update_user_profile(self):
        user = User.objects.create(username='user')
        self.assertTrue(Profile.objects.filter(user=user).exists())
