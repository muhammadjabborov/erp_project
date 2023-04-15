from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView, \
    CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.employer.models import Employer
from apps.employer.serializers import UpdateEmployerModelSerializer, \
    RetrieveEmployerModelSerializer, CreateEmployerModelSerializer, ListEmployerModelSerializer


class CreateEmployerAPIView(CreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = CreateEmployerModelSerializer
    permission_classes = (IsAdminUser,)


class ListEmployerAPIView(ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = ListEmployerModelSerializer
    permission_classes = (IsAdminUser,)


class UpdateEmployerAPIView(UpdateAPIView):
    queryset = Employer.objects.all()
    serializer_class = UpdateEmployerModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'username'


class RetrieveEmployerAPIView(RetrieveAPIView):
    queryset = Employer.objects.all()
    serializer_class = RetrieveEmployerModelSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'username'


class DestroyEmployerAPIView(DestroyAPIView):
    queryset = Employer.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = 'username'
