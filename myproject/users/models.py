from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    # Adding related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related_name for groups
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Custom related_name for permissions
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='user',
    )
