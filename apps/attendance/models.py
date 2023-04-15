from django.db import models
from django.db.models import ForeignKey, CASCADE, DateTimeField
from datetime import datetime, timezone
from apps.common.models import BaseModel


class Attendance(BaseModel):
    employer = ForeignKey('employer.Employer', CASCADE)
    start_work = DateTimeField()
    late_date = DateTimeField()

    @property
    def get_time_work(self):
        tz = timezone.utc
        now = datetime.now(tz)
        start_work = self.start_work.astimezone(tz)
        time_worked = now - start_work
        total_seconds = time_worked.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        return f"Your work time is {hours} hours, {minutes} minutes"

    @property
    def get_late_time(self):
        late_time = self.late_date - self.start_work
        return f"You late for {late_time}"

    def __str__(self):
        return self.employer.first_name

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendance'
