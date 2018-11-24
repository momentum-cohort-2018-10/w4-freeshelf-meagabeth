from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from themet.models import Book
from django.core.files import File

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'themet', 'initial_data', file)

class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting books...")
        Book.objects.all().delete()
        with open(os.path.join(settings.BASE_DIR, 'themet', 'initial_data', 'books.csv')) as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    description=row['description'],
                    # date_added=row['date_added'],
                    # category=row['category'],
                    image=row['image'],
                    # url=row['url'],
                )
                book.image.save(row['image'],
                            File(open(get_path(row['image']), 'rb')))
                book.save()
        print("Books loaded!")
