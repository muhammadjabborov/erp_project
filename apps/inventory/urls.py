from django.urls import path

from apps.inventory.views import UpdateInventoryAPIView, RetrieveInventoryAPIView, DestroyInventoryAPIView, \
    CreateInventoryAPIView, ListInventoryAPIView

urlpatterns = [
    path('create/', CreateInventoryAPIView.as_view(), name='create_inventory'),
    path('list/', ListInventoryAPIView.as_view(), name='list_inventory'),
    path('update/<int:pk>', UpdateInventoryAPIView.as_view(), name='update_inventory'),
    path('retrieve/<int:pk>', RetrieveInventoryAPIView.as_view(), name='retrieve_inventory'),
    path('destroy/<int:pk>', DestroyInventoryAPIView.as_view(), name='destroy_inventory')
]
