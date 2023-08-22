from rest_framework import serializers

from .models import Project, Contributor, Issue, Comment


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

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

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     author = request.user
    #     project = Project.objects.create(author=author, **validated_data)
    #     return project


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all(), write_only=True)
    issue_detail = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author(self, instance):
        return f'{instance.author}'

    def get_issue_detail(self, instance):
        issue = instance.issue
        issue_data = IssueSerializer(issue, context=self.context).data
        return issue_data

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        issue = validated_data.pop('issue')
        comment = Comment.objects.create(author=author, issue=issue, **validated_data)
        return comment


class IssueSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), write_only=True)
    issue_project_name = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    assign_to = serializers.PrimaryKeyRelatedField(
        queryset=Contributor.objects.none(),
        required=False,
        allow_null=True,
        write_only=True
    )
    assign_to_contributors = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = "__all__"

    def get_issue_project_name(self, instance):
        return f'{instance.project}'

    def get_author(self, instance):
        return f'{instance.project.author}'

    def get_assign_to_contributors(self, obj):
        assign_to_contributors = obj.assign_to
        if assign_to_contributors:
            return f'{assign_to_contributors}'
        return "Unassigned"

    def create(self, validated_data):
        request = self.context.get('request')
        assign_to_contributor = validated_data.pop('assign_to', None)
        author = request.user
        issue = Issue.objects.create(author=author, **validated_data)

        if assign_to_contributor:
            assign_to_project = issue.project
            if assign_to_contributor.project == assign_to_project:
                issue.assign_to = assign_to_contributor
                issue.save()

        return issue
