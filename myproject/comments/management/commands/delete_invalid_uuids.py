import os
import django
import uuid
from django.core.management.base import BaseCommand
from comments.models import Comment


# Set up Django environment with correct path formatting
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()


class Command(BaseCommand):
    help = "Check and fix invalid UUIDs in the Comment model"

    def handle(self, *args, **kwargs):
        self.stdout.write("Checking UUID validity...")

        # Initialize counters
        valid_uuids = 0
        invalid_uuids = 0

        comments = Comment.objects.all()
        for comment in comments:
            comment_id = str(comment.id)
            self.stdout.write(f"Checking Comment ID: {comment_id}")  # Debugging line

            try:
                # Attempt to validate UUID
                uuid_obj = uuid.UUID(comment_id)
                valid_uuids += 1
            except ValueError:
                self.stdout.write(self.style.ERROR(f"Invalid UUID found: {comment_id}"))
                invalid_uuids += 1

        self.stdout.write(f"Total valid UUIDs: {valid_uuids}")
        self.stdout.write(f"Total invalid UUIDs: {invalid_uuids}")

        if invalid_uuids > 0:
            self.stdout.write("Fixing invalid UUIDs...")
            for comment in comments:
                comment_id = str(comment.id)
                try:
                    # Attempt to validate UUID again
                    uuid_obj = uuid.UUID(comment_id)
                except ValueError:
                    # Fix by generating a new UUID
                    new_uuid = uuid.uuid4()
                    self.stdout.write(
                        f"Fixing Comment ID: {comment_id} -> New UUID: {new_uuid}"
                    )
                    comment.id = new_uuid
                    comment.save()

            self.stdout.write(self.style.SUCCESS("Invalid UUIDs fixed."))
        else:
            self.stdout.write(self.style.SUCCESS("No invalid UUIDs found."))
