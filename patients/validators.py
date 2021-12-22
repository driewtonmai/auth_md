from django.core.exceptions import ValidationError
from datetime import date


def validate_date_of_birth_no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Date of birth cannot be in the future.')


def validate_date_of_birth_max_age(value):
    MAX_AGE = 150
    age = (date.today() - value).days / 365
    if age > MAX_AGE:
        raise ValidationError(f'Are you Frankenstein? (Age cannot exceed {MAX_AGE})')
