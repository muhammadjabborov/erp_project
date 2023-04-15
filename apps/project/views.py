from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.project.models import Project
from apps.project.serializers import CreateProjectModelSerializer, ListProjectModelSerializer, \
    UpdateProjectModelSerializer, RetrieveProjectModelSerializer


class CreateProjectAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectModelSerializer
    permission_classes = (IsAdminUser,)


class ListProjectAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ListProjectModelSerializer
    permission_classes = (IsAdminUser,)


class UpdateProjectAPIView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = UpdateProjectModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class RetrieveProjectAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = RetrieveProjectModelSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'


class DestroyProjectAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = 'pk'
