# from rest_framework import serializers
from rest_framework import serializers

from authentification.models import UserProfile
from .models import Project, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    # register serializer
    contributor = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


