from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.inventory.models import Inventory
from apps.inventory.serializers import CreateInventoryModelSerializer, ListInventoryModelSerializer, \
    UpdateInventoryModelSerializer, RetrieveInventoryModelSerializer


class CreateInventoryAPIView(CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = CreateInventoryModelSerializer
    permission_classes = (IsAdminUser,)


class ListInventoryAPIView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = ListInventoryModelSerializer
    permission_classes = (IsAdminUser,)


class UpdateInventoryAPIView(UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = UpdateInventoryModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class RetrieveInventoryAPIView(RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = RetrieveInventoryModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class DestroyInventoryAPIView(DestroyAPIView):
    queryset = Inventory.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'
