from django.db.models import CharField, TextField, ManyToManyField, DateTimeField

from apps.common.models import BaseModel
from apps.project.choices import ProjectStatusChoices


class Project(BaseModel):
    title = CharField(max_length=255)
    description = TextField()
    employers = ManyToManyField('employer.Employer', 'employers')
    status = CharField(max_length=25, choices=ProjectStatusChoices.choices, default=ProjectStatusChoices.WAITING)
    deadline = DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'projects'
        verbose_name_plural = 'projects'
