from django.core.management.base import BaseCommand
from category.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        if Category.objects.count() == 0:
            Category.objects.create_category('Category A')
            print('Category A created.')
            Category.objects.create_category('Category B')
            print('Category B created.')
        else:
            print('Categories have already been created.')