from django.db import models
from django.db.models import CharField, TextField, ImageField, DateTimeField, BooleanField

from apps.common.models import BaseModel


class Event(BaseModel):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='%Y/%m/%d')
    start_date = DateTimeField()
    is_finished = BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Event'
