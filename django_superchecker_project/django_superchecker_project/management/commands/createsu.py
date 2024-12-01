from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
 
 
class Command(BaseCommand):
 
    def handle(self, *args, **options):
        if not User.objects.filter(username="datub22").exists():
            User.objects.create_superuser("datub22", "datu2@gmail.com", "password22")