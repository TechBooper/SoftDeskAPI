from django.db import models
from users.models import User

class Project(models.Model):
    BACKEND = 'BE'
    FRONTEND = 'FE'
    IOS = 'IOS'
    ANDROID = 'AND'
    PROJECT_TYPES = [
        (BACKEND, 'Back-End'),
        (FRONTEND, 'Front-End'),
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=PROJECT_TYPES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_time = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(User, through='Contributor', related_name='contributing_projects')

class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

class Meta:
        unique_together = ['user', 'project']