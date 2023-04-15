from django.urls import path, include

urlpatterns = [
    path('employer/', include('apps.employer.urls')),
    path('project/', include('apps.project.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('internship/', include('apps.internship.urls')),
    path('event/', include('apps.event.urls')),
    path('inventory/', include('apps.inventory.urls'))
]
