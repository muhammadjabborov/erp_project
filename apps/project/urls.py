from django.urls import path

from apps.project.views import UpdateProjectAPIView, RetrieveProjectAPIView, DestroyProjectAPIView, \
    CreateProjectAPIView, ListProjectAPIView

urlpatterns = [
    path('create/', CreateProjectAPIView.as_view(), name='create_project'),
    path('list/', ListProjectAPIView.as_view(), name='list_project'),
    path('update/<int:pk>', UpdateProjectAPIView.as_view(), name='update_project'),
    path('retrieve/<int:pk>', RetrieveProjectAPIView.as_view(), name='retrieve_project'),
    path('destroy/<int:pk>', DestroyProjectAPIView.as_view(), name='destroy_project')
]
