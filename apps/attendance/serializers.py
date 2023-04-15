from rest_framework.serializers import ModelSerializer

from apps.attendance.models import Attendance
from apps.employer.models import Employer


class EmployerModelSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'first_name', 'last_name', 'username', 'age', 'salary')


class RetrieveAttendanceModelSerializer(ModelSerializer):
    employer = EmployerModelSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ('id', 'employer', 'start_work', 'get_time_work', 'get_late_time')


class ListAttendanceModelSerializer(ModelSerializer):
    employer = EmployerModelSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ('id', 'employer', 'start_work', 'get_late_time')
