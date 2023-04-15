from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, DateTimeField

from apps.common.models import BaseModel


class Internship(BaseModel):
    title = CharField(max_length=255)
    description = TextField()
    contributors = ManyToManyField('employer.Employer', 'contributors')
    started_at = DateTimeField()
    finished_at = DateTimeField()

    class Meta:
        verbose_name = 'Internship'
        verbose_name_plural = 'Internship'
