from django.db import models
from projects.models import Project
from users.models import User
import uuid


class Issue(models.Model):
    LOW = "LOW"
    MEDIUM = "MED"
    HIGH = "HIGH"
    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"
    TAG_CHOICES = [
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (TASK, "Task"),
    ]

    TODO = "TODO"
    IN_PROGRESS = "INP"
    FINISHED = "FIN"
    STATUS_CHOICES = [
        (TODO, "To Do"),
        (IN_PROGRESS, "In Progress"),
        (FINISHED, "Finished"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(
        Project, related_name="issues", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        User,
        related_name="assigned_issues",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_time = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=10, choices=[("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High")]
    )
    label = models.CharField(
        max_length=10,
        choices=[("BUG", "Bug"), ("FEATURE", "Feature"), ("TASK", "Task")],
    )
    status = models.CharField(
        max_length=15,
        choices=[
            ("TODO", "To Do"),
            ("IN_PROGRESS", "In Progress"),
            ("FINISHED", "Finished"),
        ],
    )
