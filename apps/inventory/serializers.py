from rest_framework.serializers import ModelSerializer

from apps.inventory.models import Inventory


class CreateInventoryModelSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'title', 'quantity', 'price')


class ListInventoryModelSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'title', 'price')


class UpdateInventoryModelSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'title', 'quantity', 'price')


class RetrieveInventoryModelSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'title', 'quantity', 'price')
