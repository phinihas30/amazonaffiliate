
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Creates a superuser from environment variables with fallback options"

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-if-exists',
            action='store_true',
            help='Skip creation if any superuser already exists',
        )

    def handle(self, *args, **options):
        User = get_user_model()

        # Check if we should skip if any superuser exists
        if options['skip_if_exists'] and User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.WARNING("Superuser already exists. Skipping creation."))
            return

        # Try to get credentials from environment variables
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        # Fallback credentials if environment variables are not set
        if not all([username, email, password]):
            self.stdout.write(self.style.WARNING("Environment variables not found. Using fallback credentials."))
            username = username or "admin"
            email = email or "admin@example.com"
            password = password or "admin123"

            self.stdout.write(self.style.WARNING(
                f"Using fallback: username='{username}', email='{email}'"
            ))
            self.stdout.write(self.style.WARNING(
                "IMPORTANT: Change these credentials after first login!"
            ))

        # Check if user with this username already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
            return

        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully."))

            if not all([os.environ.get("DJANGO_SUPERUSER_USERNAME"),
                       os.environ.get("DJANGO_SUPERUSER_EMAIL"),
                       os.environ.get("DJANGO_SUPERUSER_PASSWORD")]):
                self.stdout.write(self.style.WARNING(
                    "Remember to set proper environment variables for production:"
                ))
                self.stdout.write("- DJANGO_SUPERUSER_USERNAME")
                self.stdout.write("- DJANGO_SUPERUSER_EMAIL")
                self.stdout.write("- DJANGO_SUPERUSER_PASSWORD")

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to create superuser: {e}"))
            raise
