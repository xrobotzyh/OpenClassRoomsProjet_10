import uuid as uuid
from django.db import models

from OpenClassRoomsProjet_10 import settings


class Project(models.Model):
    BACK_END = "back_end"
    FRONT_END = "front_end"
    IOS = "iOS"
    ANDROID = "Android"
    type_choices = (
        (IOS, "iOS"),
        (ANDROID, "Android"),
        (BACK_END, "back_end"),
        (FRONT_END, "front_end"),
    )
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    author = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name='created_projects')
    project_type = models.CharField(max_length=10, choices=type_choices)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="contributors")


class Issue(models.Model):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    priority_choices = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    )

    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"
    nature_choices = (
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (TASK, "Task"),
    )

    TO_DO = "To_Do"
    IN_PROGRESS = "In_Progress"
    FINISHED = "Finished"
    progress_choice = (
        (TO_DO, "To Do"),
        (IN_PROGRESS, "In Progress"),
        (FINISHED, "Finished"),
    )

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                               related_name='issue_author')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="issue")
    assign_to = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name="assign_to_author", blank=True,
                                  null=True)
    priority = models.CharField(max_length=10, choices=priority_choices)
    nature_issue = models.CharField(max_length=10, choices=nature_choices)
    status_progress = models.CharField(max_length=20, choices=progress_choice, default=TO_DO)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comment')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='project')
    description = models.CharField(max_length=2048)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_issue_link(self):
        return f'projects/{self.project_id}/issues/{self.issue.id}/'
