from datetime import datetime, timedelta

from django.core.exceptions import ValidationError

from django.test import TestCase

from .factories import DiagnoseFactory, PatientFactory


class DiagnoseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.diagnose = DiagnoseFactory()

    def test_representation_to_string(self):
        expected_str = self.diagnose.name
        self.assertEquals(self.diagnose.__str__(), expected_str)


class PatientTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        diagnoses = DiagnoseFactory.create_batch(3)
        cls.patient = PatientFactory(diagnoses=diagnoses)

    def test_representation_to_string(self):
        expected_str = f'Patient #{self.patient.id}'
        self.assertEquals(self.patient.__str__(), expected_str)

    def test_validate_date_of_birth_no_future(self):
        future_date = datetime.today().date() + timedelta(days=30)
        patient = PatientFactory.build(date_of_birth=future_date)

        with self.assertRaises(ValidationError):
            patient.full_clean()

    def test_validate_date_of_birth_max_age(self):
        patient = PatientFactory.build(date_of_birth='1800-1-1')

        with self.assertRaises(ValidationError):
            patient.full_clean()