from django.contrib.auth.models import User

import factory
from django.db.models.signals import post_save
from factory.django import DjangoModelFactory

from authentication.models import Profile


@factory.django.mute_signals(post_save)
class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    is_doctor = False
    user = factory.SubFactory('authentication.tests.factories.UserFactory', profile=None)


@factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttributeSequence(lambda obj, n: f'{obj.username}@gmail.com')
    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')
    password = factory.PostGenerationMethodCall('set_password', '1234')
