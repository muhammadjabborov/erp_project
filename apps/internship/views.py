from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.internship.models import Internship
from apps.internship.serializers import CreateInternshipModelSerializer, ListInternshipModelSerializer, \
    UpdateInternshipModelSerializer, RetrieveInternshipModelSerializer


class CreateInternshipAPIView(CreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = CreateInternshipModelSerializer
    permission_classes = (IsAdminUser,)


class ListInternshipAPIView(ListAPIView):
    queryset = Internship.objects.all()
    serializer_class = ListInternshipModelSerializer
    permission_classes = (IsAdminUser,)


class UpdateInternshipAPIView(UpdateAPIView):
    queryset = Internship.objects.all()
    serializer_class = UpdateInternshipModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class RetrieveInternshipAPIView(RetrieveAPIView):
    queryset = Internship.objects.all()
    serializer_class = RetrieveInternshipModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class DestroyInternshipAPIView(DestroyAPIView):
    queryset = Internship.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'
