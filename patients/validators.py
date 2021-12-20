from django.core.exceptions import ValidationError
from datetime import date


def validate_date_of_birth_no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Date of birth cannot be in the future.')
