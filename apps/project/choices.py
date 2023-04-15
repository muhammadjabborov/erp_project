from django.db.models import TextChoices


class ProjectStatusChoices(TextChoices):
    WAITING = "waiting"
    PROGRESS = "in progress"
    FINISHED = "is finished"
