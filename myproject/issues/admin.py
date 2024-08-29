from django.contrib import admin
from .models import Issue  # Import your Issue model
# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'author', 'assignee', 'created_time')
    search_fields = ('title', 'description')

admin.site.register(Issue)