from rest_framework.serializers import ModelSerializer

from apps.employer.models import Employer


class CreateEmployerModelSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'first_name', 'last_name', 'username', 'age', 'position', 'salary', 'is_active')


class ListEmployerModelSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'first_name', 'last_name', 'username', 'age', 'position', 'salary', 'is_active')


class UpdateEmployerModelSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'first_name', 'last_name', 'username', 'age', 'position', 'salary', 'is_active')


class RetrieveEmployerModelSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'first_name', 'last_name', 'username', 'age', 'position', 'salary', 'is_active')
