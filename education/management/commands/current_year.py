import datetime
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        current_y = datetime.date.today()
        yearis = (str(current_y.year))
        return yearis 
        
    