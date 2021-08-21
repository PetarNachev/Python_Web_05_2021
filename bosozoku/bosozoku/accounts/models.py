from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from bosozoku.accounts.managers import BosozokuUserManager

from cloudinary import models as cloudinary_models

class BosozokuUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = 'email'

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = BosozokuUserManager()


class Profile(models.Model):
    profile_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )
    user = models.OneToOneField(
        BosozokuUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
