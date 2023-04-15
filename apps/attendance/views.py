from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from apps.attendance.models import Attendance
from apps.attendance.serializers import RetrieveAttendanceModelSerializer, ListAttendanceModelSerializer


class RetrieveAttendanceAPIView(RetrieveAPIView):
    queryset = Attendance.objects.order_by('-created_at')
    serializer_class = RetrieveAttendanceModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class ListAttendanceAPIView(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = ListAttendanceModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'

