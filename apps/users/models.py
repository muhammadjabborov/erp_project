from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True)
    avatar = models.ImageField(upload_to="users/%Y/%m/", blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
