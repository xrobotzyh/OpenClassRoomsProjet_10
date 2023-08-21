from rest_framework import serializers

from authentification.serializers import UserSerializer
from .models import Project, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = ['user']


class ProjectSerializer(serializers.ModelSerializer):
    # register serializer
    contributors = ContributorSerializer(many=True, required=False)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = "__all__"

