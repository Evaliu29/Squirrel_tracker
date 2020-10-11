from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path',type=str,help='csv file')

    def handle(self,path,**options):

        with open(path, 'w',newline = '') as csvfile:
            writer = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
        # write your header first
            fields = [f.name for f in Squirrel._meta.fields]
            writer.writerow(fields)
            for obj in Squirrel.objects.all():
                writer.writerow(getattr(obj,f) for f in fields)
