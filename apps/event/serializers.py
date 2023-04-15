from rest_framework.serializers import ModelSerializer

from apps.event.models import Event


class CreateEventModelSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'image', 'start_date')


class ListEventModelSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'image', 'start_date', 'is_finished')


class UpdateEventModelSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'image', 'start_date', 'is_finished')


class RetrieveEventModelSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'image', 'start_date', 'is_finished')
