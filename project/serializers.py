from rest_framework import serializers

from authentification.models import UserProfile
from .models import Project, Contributor, Issue, Comment


class ContributorSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()

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

    def update(self, instance, validated_data):
        contributors_data = validated_data.pop('contributors', None)

        if contributors_data is not None:
            instance.contributors.all().delete()

            added_users = set()

            for contributor_data in contributors_data:
                user_id = contributor_data['user']

                if user_id not in set():
                    try:
                        user = UserProfile.objects.get(username=user_id)
                        Contributor.objects.create(project=instance, user=user)
                        added_users.add(user_id)
                    except UserProfile.DoesNotExist:
                        pass

        return super().update(instance, validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description', 'project_id', 'issue_id', 'uuid', 'author_id']
        read_only_fields = ['project_id', 'issue_id', 'uuid', 'author_id']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'priority', 'nature_issue', 'assign_to', 'status_progress', 'author']
        read_only_fields = ['id', 'author']

    def validate_assign_to(self, value):
        project_id = self.context["view"].kwargs["project_id"]
        contributors = Contributor.objects.filter(project_id=project_id).all()

        contributors_id = []
        for contributor in contributors:
            contributors_id.append(contributor.user_id)
        if value.id not in contributors_id:
            raise serializers.ValidationError("Assignee must be a contributor of this project.")

        return value

# class IssueSerializer(serializers.ModelSerializer):
#     assign_to = serializers.StringRelatedField()
#
#     class Meta:
#         model = Issue
#         fields = '__all__'


# class IssueSerializer(serializers.ModelSerializer):
#     contributors = ContributorSerializer(many=True, required=False)
#     project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), write_only=True)
#     issue_project_name = serializers.SerializerMethodField()
#     author = serializers.StringRelatedField()
#     assign_to = serializers.PrimaryKeyRelatedField(
#         queryset=Contributor.objects.none(),
#         required=False,
#         allow_null=True,
#     )
#     assign_to_contributors = serializers.SerializerMethodField()
#     comments = CommentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Issue
#         fields = "__all__"
#
#     def get_issue_project_name(self, instance):
#         return f'{instance.project}'
#
#     def get_author(self, instance):
#         return f'{instance.project.author}'
#
#     def get_assign_to_contributors(self, obj):
#         assign_to_contributors = obj.assign_to
#
#         if assign_to_contributors:
#             return f'{assign_to_contributors}'
#
#         return "Unassigned"
#
#     def create(self, validated_data):
#         request = self.context.get('request')
#         assign_to_contributor = validated_data.pop('assign_to', None)
#         author = request.user
#         issue = Issue.objects.create(author=author, **validated_data)
#
#         if assign_to_contributor:
#             assign_to_project = issue.project
#             if assign_to_contributor.project == assign_to_project:
#                 issue.assign_to = assign_to_contributor
#                 issue.save()
#
#         return issue
