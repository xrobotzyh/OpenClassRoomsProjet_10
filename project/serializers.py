# from rest_framework import serializers
from rest_framework import serializers

from authentification.models import UserProfile
from .models import Project, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # project = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Contributor
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    # register serializer
    contributor = ContributorSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

# class IssueSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
#
#     class Meta:
#         model = Contributor
#         fields = '__all__'
