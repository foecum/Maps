from django.core.management.base import BaseCommand

from shortener.models import GittaURL

class Command(BaseCommand):
    help="Refreshes all GittaURL shortcodes"

    def handle(self, *args, **options):
        return GittaURL.objects.refresh_shortcodes()
