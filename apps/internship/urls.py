from django.urls import path

from apps.internship.views import UpdateInternshipAPIView, RetrieveInternshipAPIView, DestroyInternshipAPIView, \
    CreateInternshipAPIView, ListInternshipAPIView

urlpatterns = [
    path('create/', CreateInternshipAPIView.as_view(), name='create_internship'),
    path('list/', ListInternshipAPIView.as_view(), name='list_internship'),
    path('update/<int:pk>', UpdateInternshipAPIView.as_view(), name='update_internship'),
    path('retrieve/<int:pk>', RetrieveInternshipAPIView.as_view(), name='retrieve_internship'),
    path('destroy/<int:pk>', DestroyInternshipAPIView.as_view(), name='destroy_internship')
]
