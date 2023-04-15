from rest_framework.serializers import ModelSerializer

from apps.internship.models import Internship


class CreateInternshipModelSerializer(ModelSerializer):
    class Meta:
        model = Internship
        fields = ('id', 'title', 'description', 'contributors', 'started_at', 'finished_at')


class ListInternshipModelSerializer(ModelSerializer):
    class Meta:
        model = Internship
        fields = ('id', 'title', 'contributors')


class UpdateInternshipModelSerializer(ModelSerializer):
    class Meta:
        model = Internship
        fields = ('id', 'title', 'description', 'contributors', 'started_at', 'finished_at')


class RetrieveInternshipModelSerializer(ModelSerializer):
    class Meta:
        model = Internship
        fields = ('id', 'title', 'description', 'contributors', 'started_at', 'finished_at')
