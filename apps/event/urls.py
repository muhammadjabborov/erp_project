from django.urls import path

from apps.event.views import UpdateEventAPIView, RetrieveEventAPIView, DestroyEventAPIView, \
    CreateEventAPIView, ListEventAPIView

urlpatterns = [
    path('create/', CreateEventAPIView.as_view(), name='create_event'),
    path('list/', ListEventAPIView.as_view(), name='list_event'),
    path('update/<int:pk>', UpdateEventAPIView.as_view(), name='update_event'),
    path('retrieve/<int:pk>', RetrieveEventAPIView.as_view(), name='retrieve_event'),
    path('destroy/<int:pk>', DestroyEventAPIView.as_view(), name='destroy_event')
]
