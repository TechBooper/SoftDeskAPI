from django.db import models
from projects.models import Project
from users.models import User

class Issue(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MED'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    BUG = 'BUG'
    FEATURE = 'FEATURE'
    TASK = 'TASK'
    TAG_CHOICES = [
        (BUG, 'Bug'),
        (FEATURE, 'Feature'),
        (TASK, 'Task'),
    ]

    TODO = 'TODO'
    IN_PROGRESS = 'INP'
    FINISHED = 'FIN'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_issues')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_issues')
    priority = models.CharField(max_length=5, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
    created_time = models.DateTimeField(auto_now_add=True)