from datetime import datetime

import factory.fuzzy
import factory
from factory.django import DjangoModelFactory

from patients.models import Diagnose, Patient


class DiagnoseFactory(DjangoModelFactory):
    class Meta:
        model = Diagnose

    name = factory.Sequence(lambda n: f'diagnose {n}')


class PatientFactory(DjangoModelFactory):
    class Meta:
        model = Patient

    date_of_birth = factory.fuzzy.FuzzyDate(
        datetime(1940, 1, 1).date(),
        datetime.today().date(),
    )

    @factory.post_generation
    def diagnoses(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for diagnose in extracted:
                self.diagnoses.add(diagnose)
