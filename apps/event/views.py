from rest_framework.generics import DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAdminUser

from apps.event.models import Event
from apps.event.serializers import RetrieveEventModelSerializer, CreateEventModelSerializer, ListEventModelSerializer, \
    UpdateEventModelSerializer


class CreateEventAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = CreateEventModelSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAdminUser,)


class ListEventAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = ListEventModelSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAdminUser,)


class UpdateEventAPIView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = UpdateEventModelSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class RetrieveEventAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = RetrieveEventModelSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class DestroyEventAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'
