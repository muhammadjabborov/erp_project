from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from config.schema import schema_urlpatterns
from config.settings import develop as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', TokenObtainPairView.as_view(), name='login_auth'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='refresh_auth'),
    path('api/v1/', include('apps.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += schema_urlpatterns
