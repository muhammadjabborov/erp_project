from rest_framework.serializers import ModelSerializer

from apps.project.models import Project


class CreateProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'employers', 'status', 'deadline')


class ListProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'deadline')


class UpdateProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'employers', 'status', 'deadline')


class RetrieveProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'employers', 'status', 'deadline')

