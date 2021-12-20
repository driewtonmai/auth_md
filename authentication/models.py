from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    is_doctor = models.BooleanField('is doctor', default=False)

    def __str__(self):
        return f'Profile for user {self.user.username}'

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
