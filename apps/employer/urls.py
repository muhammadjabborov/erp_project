from django.urls import path

from apps.employer.views import UpdateEmployerAPIView, RetrieveEmployerAPIView, DestroyEmployerAPIView, \
    CreateEmployerAPIView, ListEmployerAPIView

urlpatterns = [
    path('create/', CreateEmployerAPIView.as_view(), name='create_employer'),
    path('list/', ListEmployerAPIView.as_view(), name='list_employer'),
    path('update/<str:username>', UpdateEmployerAPIView.as_view(), name='update_employer'),
    path('retrieve/<str:username>', RetrieveEmployerAPIView.as_view(), name='retrieve_employer'),
    path('destroy/<str:username>', DestroyEmployerAPIView.as_view(), name='destroy_employer')
]
