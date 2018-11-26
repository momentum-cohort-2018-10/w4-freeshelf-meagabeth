from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import json
from themet.models import Book
from django.core.files import File
from django.template.defaultfilters import slugify


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
        i = 0
        with open(get_path('books.json'), 'r') as file:
            reader = json.load(file)
            for book in reader:
                book = Book(
                    title=reader[i]['title'],
                    author=reader[i]['author'],
                    description=reader[i]['description'],
                    # date_added=reader['date_added'],
                    # category=reader['category'],
                    # image=reader['image'],
                    url=reader[i]['url'],
                    slug=slugify(reader[i]['title']),
                    african_art=reader[i]['african_art'],
                    american_art=reader[i]['american_art'],
                    medival_art=reader[i]['medival_art'],
                    european_art=reader[i]['european_art'],
                    twentieth_cent_art=reader[i]['twentieth_cent_art']

                )
                # book.image.save(row['image'],
                #             File(open(get_path(row['image']), 'rb')))
                book.save()
                i += 1
        print("Books loaded!")
