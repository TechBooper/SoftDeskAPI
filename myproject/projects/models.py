from django.db import models
from django.conf import (
    settings,
)


class Project(models.Model):
    BACKEND = "BE"
    FRONTEND = "FE"
    IOS = "IOS"
    ANDROID = "AND"
    PROJECT_TYPES = [
        (BACKEND, "Back-End"),
        (FRONTEND, "Front-End"),
        (IOS, "iOS"),
        (ANDROID, "Android"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=PROJECT_TYPES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="projects"
    )


class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "project"]
