from rest_framework import serializers

from authentification.models import UserProfile
from .models import Project, Contributor, Issue, Comment


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user']


class ProjectSerializer(serializers.ModelSerializer):
    # register serializer
    contributors = ContributorSerializer(many=True, required=False)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Project
        fields = "__all__"

    # re write the create method, if user enter several contributors at a time
    def create(self, validated_data):
        contributors_data = validated_data.pop('contributors', None)
        project = Project.objects.create(**validated_data)

        if contributors_data is not None:
            for contributor_data in contributors_data:
                user_id = contributor_data['user']
                try:
                    user = UserProfile.objects.get(username=user_id)
                    Contributor.objects.create(project=project, user=user)
                except UserProfile.DoesNotExist:
                    pass

        return project

    # re write the update method, if user enter several contributors at a time
    def update(self, instance, validated_data):
        contributors_data = validated_data.pop('contributors', None)

        if contributors_data is not None:
            instance.contributors.all().delete()

            for contributor_data in contributors_data:
                user_id = contributor_data['user']
                if user_id not in set():
                    try:
                        user = UserProfile.objects.get(username=user_id)
                        Contributor.objects.create(project=instance, user=user)
                    except UserProfile.DoesNotExist:
                        pass

        return super().update(instance, validated_data)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'priority', 'nature_issue', 'assign_to', 'status_progress', 'author']
        read_only_fields = ['id', 'author']

    # assign to must be a action to a contributor
    def validate_assign_to(self, value):
        if value is not None and value.id is not None:
            project_id = self.context["view"].kwargs["project_id"]
            contributors = Contributor.objects.filter(project_id=project_id).all()

            contributors_id = []
            for contributor in contributors:
                contributors_id.append(contributor.user_id)
            if value.id not in contributors_id:
                raise serializers.ValidationError("Assignee must be a contributor of this project.")

        return value


class CommentSerializer(serializers.ModelSerializer):
    issue_link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'description', 'project_id', 'issue_id', 'uuid', 'author_id', 'issue_link']
        read_only_fields = ['id', 'project_id', 'issue_id', 'uuid', 'author_id']

    # give the detail page url
    def get_issue_link(self, instance):
        return f'api/projects/{instance.project_id}/issues/{instance.issue.id}/'
