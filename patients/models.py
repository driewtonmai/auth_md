from django.db import models

from .validators import validate_date_of_birth_no_future, validate_date_of_birth_max_age


class Diagnose(models.Model):
    """Model for diagnoses"""

    name = models.CharField('name', max_length=70, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'diagnose'
        verbose_name_plural = 'Diagnoses'


class Patient(models.Model):
    """Model for patients"""

    date_of_birth = models.DateField('date of birth',
                                     validators=[validate_date_of_birth_no_future, validate_date_of_birth_max_age])
    diagnoses = models.ManyToManyField(Diagnose,
                                       verbose_name='diagnoses', related_name='patients', blank=True)
    created_at = models.DateTimeField('date of creation', auto_now_add=True)

    def __str__(self):
        return f'Patient #{self.id}'

    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'Patients'
        ordering = ['-created_at']
