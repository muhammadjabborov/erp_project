from django.urls import path

from apps.attendance.views import RetrieveAttendanceAPIView, ListAttendanceAPIView

urlpatterns = [
    path('<int:pk>/', RetrieveAttendanceAPIView.as_view(), name='retrieve_attendance'),
    path('list/', ListAttendanceAPIView.as_view(), name='list_attendance')
]
