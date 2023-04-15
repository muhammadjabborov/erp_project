from django.db import models
from django.db.models import CharField, IntegerField, FloatField, DecimalField, BooleanField
from apps.common.models import BaseModel


class Employer(BaseModel):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    age = IntegerField()
    position = CharField(max_length=255)
    salary = DecimalField(max_digits=10, decimal_places=6)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employer'
